import streamlit as st
from agent import ToolAgent

st.title("🔧 Manual Tool Routing Agent")

goal = st.text_input("Enter your goal")

if st.button("Run Agent"):
    agent = ToolAgent()
    result = agent.run(goal)
    st.write(result)