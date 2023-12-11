# sss

from functions import *


def get_command():
    command = input("<")
    blank_line = command.find(" ")
    if blank_line == -1:
        return command
    command_to_execute = command[:blank_line]
    argument_1 = command[blank_line + 1:]
    blank_line = argument_1.find(" ")
    if blank_line == -1:
        return command_to_execute, argument_1
    argument_2 = argument_1[blank_line + 1:]
    argument_1 = argument_1[:blank_line]
    blank_line = argument_2.find(" ")
    if blank_line == -1:
        return command_to_execute, [argument_1, argument_2]
    argument_3 = argument_2[blank_line + 1:]
    argument_2 = argument_2[:blank_line]
    blank_line = argument_3.find(" ")
    if blank_line == -1:
        return command_to_execute, [argument_1, argument_2, argument_3]
    else:
        print("Invalid command type")
        return 0, 0


def add_products(all_products, name, quantity, price):
    try:
        quantity = int(quantity)
        price = int(price)
        if price < 1 or quantity < 1:
            raise ValueError("Not positive integers")
        add_product(all_products, name, quantity, price)
    except ValueError as ve:
        print(ve)


def delete_products(all_products, name):
    try:
        is_there = 0
        name = str(name)
        for products in all_products:
            if products["name"] == name:
                is_there += 1
        if is_there == 0:
            raise ValueError("Product not there")
        all_products = delete_product(all_products, name)
        return all_products
    except ValueError as ve:
        print(ve)


def list_all_products(all_products):
    # print(*all_products,sep='\n')
    new_list = sorted(all_products, key=lambda products: products["name"])
    print(*new_list, sep='\n')


def list_total_value_of_warehouse(all_products):
    total_value = 0
    for products in range(len(all_products)):
        total_value = total_value + all_products[products]["quantity"] * all_products[products]["price"]
    print(total_value)


def print_options():
    print("add a product")
    print("remove a product")
    print("list all")
    print("list total")
    print("exit fast")


def run_console():
    all_products = []
    while True:
        print_options()
        command_to_run, arguments = get_command()
        if command_to_run == "add" and len(arguments) == 3:
            add_products(all_products, *arguments)
        if command_to_run == "add" and len(arguments) != 3:
            print("Command is not okay")
        if command_to_run == "list" and arguments == "all":
            list_all_products(all_products)
        if command_to_run == "remove":
            all_products = delete_products(all_products, arguments[0])
        if command_to_run == "list" and arguments == "total":
            list_total_value_of_warehouse(all_products)
        if command_to_run == "exit fast":
            break
