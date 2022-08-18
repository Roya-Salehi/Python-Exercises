st = input("Enter a string: ")
st_rev = st[::-1]
print(f"{st.capitalize()} is a palindrome.") if st == st_rev else print(
    f"{st.capitalize()} is not a palindrome.")

# *** A simpler solution ***
# pali = "is" if st == st_rev else "is not"
# print(f"{st.capitalize()} {pali} a palindrome.")