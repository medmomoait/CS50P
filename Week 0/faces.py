def main():
    user_input = input("Typer here: ")
    user = user_input.replace(':)', '🙂').replace(':(','🙁')
    print(user)


main()