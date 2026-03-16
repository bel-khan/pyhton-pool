# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bel-khan <bel-khan@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/19 00:50:39 by bel-khan          #+#    #+#              #
#    Updated: 2026/01/03 14:49:41 by bel-khan         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
    x = int (input("Day 1 harvest: "))
    y = int (input("Day 2 harvest: "))
    z = int (input("Day 3 harvest: "))
    print("Total harvest: ",x + y + z)


ft_harvest_total()