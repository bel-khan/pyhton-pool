# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bel-khan <bel-khan@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/19 00:50:55 by bel-khan          #+#    #+#              #
#    Updated: 2025/12/19 00:50:57 by bel-khan         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
    x =int (input("Enter plant age in days: "))
    if x >= 60 :
        print("Plant is ready to harvest!")
    else :
        print("Plant needs more time to grow.")

if __name__ == "__main__":
    ft_plant_age()