from assets import *

center_title("s", 70,"green","Send Files")


st.session_state.code = otp_gen()
center_title("s", 90,"Black", st.session_state.code)
x = st.file_uploader(accept_multiple_files=True, label="Upload Here")

if x:
    os.mkdir(st.session_state.code)
    save_directory = f"shares/{st.session_state.code}"  # Change to your desired directory path
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)


for uploaded_file in x:
    with open(os.path.join(save_directory, uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Saved file: {uploaded_file.name}")

