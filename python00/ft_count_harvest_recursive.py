# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bel-khan <bel-khan@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/19 00:50:17 by bel-khan          #+#    #+#              #
#    Updated: 2025/12/19 00:50:18 by bel-khan         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def  ft_count_harvest_recursive():
    x = int (input("Days until harvest: "))
    ft_count_recursive(1, x)
    
    print("Harvest time!")

def	ft_count_recursive(day, days):
    if day > days :
        return
    print("Day ",day)
    ft_count_recursive(day + 1,days)
    
if __name__ == "__main__":
    ft_count_harvest_recursive()
    