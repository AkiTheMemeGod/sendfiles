from assets import *

center_title("s", 70, "green", "Receive Files")

# Input for the share code
code = st.number_input(label="Enter the Code",
                       placeholder="6 Digit Share Code",
                       max_value=999999,
                       format="%d",
                       step=1)

# Check if the code directory exists
if str(code).zfill(6) in os.listdir("shares"):
    code_dir = f"shares/{str(code).zfill(6)}"
    files = os.listdir(code_dir)

    # Display download buttons for each file in the directory
    for file in files:
        file_path = os.path.join(code_dir, file)
        with open(file_path, "rb") as f:
            st.download_button(label=file, data=f, file_name=file)
else:
    st.warning("Code not found. Please check the code and try again.")
