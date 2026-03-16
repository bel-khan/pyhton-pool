# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bel-khan <bel-khan@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/19 00:49:50 by bel-khan          #+#    #+#              #
#    Updated: 2025/12/19 00:49:54 by bel-khan         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    if unit == "packets":
        print(f"{seed_type} seeds: {quantity} {unit} available")
    elif unit == "grams":
        print(f"{seed_type} seeds: {quantity} {unit} total")
    elif unit == "area":
        print(f"{seed_type} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")

if __name__ == "__main__":
    ft_seed_inventory("gorgers",15,"grams")
