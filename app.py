import streamlit as st
from game.turn_manager import TurnManager
from game.decisions import DECISION_OPTIONS

st.set_page_config(layout="wide")

st.title("⚔️ WWII Strategic Counterfactual Simulator")

# ----------------------------
# ROLE SELECTION
# ----------------------------

if "game" not in st.session_state:
    role = st.selectbox(
        "Choose Your Role",
        ["Germany", "Allies", "Japan", "USSR"]
    )

    if st.button("Start Simulation"):
        st.session_state.game = TurnManager(role)
        st.rerun()

else:
    game = st.session_state.game

    col1, col2 = st.columns(2)

    # ----------------------------
    # LEFT PANEL – PLAYER DECISIONS
    # ----------------------------

    with col1:
        st.subheader(f"🎖 Role: {game.world.role}")
        st.write(f"Turn: {game.world.turn}")

        available = game.get_available_player_decisions()

        if available:
            st.subheader("Available Decisions")

            selected_node = st.selectbox(
                "Choose Decision",
                available
            )

            choice = st.radio(
                "Choose Action",
                options=list(DECISION_OPTIONS[selected_node].keys()),
                format_func=lambda x: DECISION_OPTIONS[selected_node][x]
            )

            if st.button("Execute Decision"):
                game.player_move(selected_node, choice)
                st.rerun()

        else:
            st.success("No more decisions available.")

    # ----------------------------
    # RIGHT PANEL – WORLD STATE
    # ----------------------------

    with col2:
        st.subheader("🌍 World State")

        axis_prob = game.get_axis_victory_probability()

        st.metric(
            label="Axis Victory Probability",
            value=f"{axis_prob:.3f}"
        )

        st.subheader("Decision History")

        for event in game.world.history:
            actor = event["actor"]
            node = event["node"]
            value = event["value"]

            st.write(
                f"Turn {event['turn']} | {actor} → {node} = {value}"
            )

    # ----------------------------
    # RESET BUTTON
    # ----------------------------

    st.divider()

    if st.button("Reset Simulation"):
        del st.session_state.game
        st.rerun()