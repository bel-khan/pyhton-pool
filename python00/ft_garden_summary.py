# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_summary.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bel-khan <bel-khan@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/19 00:50:28 by bel-khan          #+#    #+#              #
#    Updated: 2025/12/19 00:50:31 by bel-khan         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_garden_summary():
    c = input("Enter garden name: ")
    x = int (input("Enter number of plants: "))
    print ("Grden:",c)
    print ("Plants:",x)
    print ("Status: Growing well! ")

if __name__== "__main__":
    ft_garden_summary()