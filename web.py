"""Script to code the Web App"""
# Run the App in terminal: streamlit run "a:/04. Cursos/17. Python Mega Course Udemy/App1_WEB/web.py"
import streamlit as st
from Modules import functions as f

todos = f.get_todos()

def add_todo():
    """Function to add a new Todo entered by users"""
    captured_todo = st.session_state["new_todo"]
    todos.append(captured_todo.strip() + "\n")
    f.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my Todo App")
st.write("This app is to increase productivity ;)")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        f.write_todos(todos)
        del st.session_state[todo] #Delete also the todo from the Session_state dict.
        st.rerun() #To update the checkboxes

st.text_input(label= " ",placeholder="Add new Todo and Hit Enter",
              on_change=add_todo, key="new_todo") #Key = Key of the "dict" st.session_state. To see write: st.session_state in a new line
#st.session_state
st.write("Developed by: Al")

#To create requirements.txt ->   pip freeze > requirements.txt