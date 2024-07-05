import streamlit as st
import optimized_5_functions

todos = optimized_5_functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    optimized_5_functions.write_todos(todos)

st.title("My todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase the productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        optimized_5_functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo..", on_change=add_todo, key='new_todo')

st.session_state