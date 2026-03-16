# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bel-khan <bel-khan@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/19 00:50:03 by bel-khan          #+#    #+#              #
#    Updated: 2025/12/19 00:50:05 by bel-khan         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    x = int (input("Days until harvest: "))
    for i in range(1,x + 1):
        print("Day: ",i)

    print("Harvest time! ")

if __name__ =="__main__":
    ft_count_harvest_iterative()