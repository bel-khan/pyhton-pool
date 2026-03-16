# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bel-khan <bel-khan@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/19 00:51:10 by bel-khan          #+#    #+#              #
#    Updated: 2025/12/19 00:51:11 by bel-khan         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
    x = int (input("Days since last watering: "))
    if x <= 2 :
        print("Plants are fine")
    else :
        print("Water the plants!")
        