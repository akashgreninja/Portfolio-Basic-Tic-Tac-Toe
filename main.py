import random


# article on how to print the text like a matrix is here https://www.geeksforgeeks.org/python-printing-list-vertically/


test_list = [["|", "|", "|"], ["|", "|", "|"], ["|", "|", "|"]]





def print_one():
       for i in range(len(test_list)):
              for z in test_list:
                 print(z[i],end =' ')
              print()


def game_over():
       if test_list[0][0]==0 and test_list[0][1]==0 and test_list[0][2] ==0:
              print("game overrrr player 1 wins")
              return("True")

       elif test_list[0][0]==0 and test_list[1][0]==0 and test_list[2][0] ==0:
              print("game overrrr player 1 wins")
              return("True")

       elif test_list[0][0]==0 and test_list[1][1]==0 and test_list[2][2] ==0:
              print("game overrrr player 1 wins")
              return("True")

       elif test_list[2][0] == 0 and test_list[1][1] == 0 and test_list[0][2] == 0:
              print("game overrrr player 1 wins")
              return ("True")

       elif test_list[0][1] == 0 and test_list[1][1] == 0 and test_list[2][1] == 0:
              print("game overrrr player 1 wins")
              return ("True")

       elif test_list[0][1] == 0 and test_list[1][2] == 0 and test_list[2][2] == 0:
              print("game overrrr player 1 wins")
              return ("True")


       elif test_list[0][0]==1 and test_list[0][1]==1 and test_list[0][2] ==1:
              print("game overrrr player 2 wins")
              return("True")

       elif test_list[0][0]==1 and test_list[1][0]==1 and test_list[2][0] ==1:
              print("game overrrr player 2 wins")
              return("True")

       elif test_list[0][0]==1 and test_list[1][1]==1 and test_list[2][2] ==1:
              print("game overrrr player 2 wins")
              return("True")

       elif test_list[2][0] == 1 and test_list[1][1] == 1 and test_list[0][2] == 1:
              print("game overrrr player 2 wins")
              return ("True")

       elif test_list[0][1] == 1 and test_list[1][1] == 1 and test_list[2][1] == 1:
              print("game overrrr player 2 wins")
              return ("True")

       elif test_list[0][1] == 1 and test_list[1][2] == 1 and test_list[2][2] == 1:
              print("game overrrr player 2 wins")
              return ("True")










def insert():
       end_of_game = False
       while end_of_game==False:
              the_row = (int(input("which row"))-1)
              which_column = (int(input("which column"))-1)
              try:
                     if type(test_list[the_row][which_column])==str:
                            test_list[the_row][which_column]=0

                     else:
                            print("You have already added here ")
                            the_row = (int(input("which row")) - 1)
                            which_column = (int(input("which column")) - 1)
                            test_list[the_row][which_column] = 0

                     print_one()

              except IndexError:
                     print("please select properly try again ")
                     the_row = (int(input("which row")) - 1)
                     which_column = (int(input("which column")) - 1)

                     test_list[the_row][which_column] = 0
                     print_one()
              finally:
                     game_over()
                     if game_over() == "True":
                            break
              the_row_1 = (int(input("which row"))-1)
              which_column_1 = (int(input("which column"))-1)

              try:
                     if type(test_list[the_row_1][which_column_1]) == str:
                            test_list[the_row_1][which_column_1]=1
                            print_one()
                     else:
                            print("You have already added here ")
                            the_row_1 = (int(input("which row")) - 1)
                            which_column_1 = (int(input("which column")) - 1)
                            test_list[the_row_1][which_column_1] = 1
                            print_one()


              except IndexError:
                     print("please select properly try again ")
                     the_row_1 = (int(input("which row")) - 1)
                     which_column_1 = (int(input("which column")) - 1)
                     test_list[the_row_1][which_column_1] = 1
                     print_one()

              finally:
                     game_over()
                     if game_over()=="True":
                            break





def start_game():
       insert()
start_game()


