quantity_of_decoration = int(input())
days_left = int(input())

ornament_set_price, ornament_set_s_points = 2, 5
tree_skirt_price, tree_skirt_s_points = 5, 3
tree_garland_price, tree_garland_s_points = 3, 10
tree_lights_price, tree_light_s_points = 15, 17

# s_points = spirit_p_earned

total_coast = 0
spirit_p_earned = 0

for current_day in range(1, days_left + 1):
    if current_day % 11 == 0:
        quantity_of_decoration += 2

    if current_day % 2 == 0:
        total_coast += ornament_set_price * quantity_of_decoration
        spirit_p_earned += ornament_set_s_points

    if current_day % 3 == 0:
        total_coast += (tree_skirt_price + tree_garland_price) * quantity_of_decoration
        spirit_p_earned += (tree_skirt_s_points + tree_garland_s_points)

    if current_day % 5 == 0:
        total_coast += tree_lights_price * quantity_of_decoration
        spirit_p_earned += tree_light_s_points
        if current_day % 3 == 0:
            spirit_p_earned += 30 # bonus points

    if current_day % 10 == 0:
        spirit_p_earned -= 20 # decrease points
        total_coast += (tree_skirt_price + tree_garland_price + tree_lights_price)

if days_left % 10 == 0:
    spirit_p_earned -= 30 # decrease points

print(f'Total cost: {total_coast}\nTotal spirit: {spirit_p_earned}')
