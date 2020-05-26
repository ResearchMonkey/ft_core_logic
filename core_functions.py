import csv
import datetime


def break_target_location(target_name_num, value):
    print(target_name_num)
    target_name_num = value.split("_")
    degree_from_zero = target_name_num[0]
    print(f'Target is at {degree_from_zero} degrees from shooter ')
    distance_from_zero = target_name_num[1]
    print(f'{distance_from_zero} inches away,')
    hight_above_zero = target_name_num[2]
    print(f'The top of the target is {hight_above_zero} above the ground')
    facing_angle = target_name_num[3]
    print(f'facing {facing_angle} degrees')
    angle_of_rotation = target_name_num[4]
    print(f'Angle of target is {angle_of_rotation} degrees\n')
    # TODO crate a dictionary from this based off target_name_num

# cof_id,name,min_rd_count,max_distance,field of fire,number_of_targets,target_001_type,target_001_positions,target_002_type,target_002_positions,starting_position,firing positions,starting conditions,reloads,transition,Movement,Judgement,failure simulations,scoring,instructions


cof_selected = {'cof_id': 1,
                'name': 'F.A.S.T Drill',
                'min_rd_count': 14,
                'max_distance': '7 yards',
                'field of fire': 180,
                'number_of_targets': 2,
                'target_001_type': '3x5',
                'target_001_positions': '360_252_70_180_0',
                'target_002_type': 'circle 8in',
                'target_002_positions': '360_252_60_180_0',
                'starting_position': 'holstered',
                'firing positions': 1,
                'starting conditions': 'loaded_chambered_Y_1',
                'reloads': 1,
                'transition': 0,
                'Movement': 0,
                'Judgement': 0,
                'failure simulations': 0,
                'scoring': 1,
                'instructions': "You will start with your weapon holstered and chambered, with 1(one) round in the magizine. You will have a second magizine loaded with 4 (four) rounds in a carrier. On the command to fire you will 1. Draw from concealment, 2. fire 2 rounds on target 1, 3. reload - slide-lock, 4. fire 4 on target 2. Then make clear and holster your weapon"}


for key, value in cof_selected.items():
    if '_positions' in key:
        # print(value)
        break_target_location(f'{key}', value)
    if 'number_of_targets' in key:
        print(f'There are {value} Targets')




# break_target_location('target_round_001', '360_000_70_180_0')

# Splash screen, user is show
# # a filterable list of history combined skills results
# # a recommended drill based on the worst skill or any skill with no score (order of skill to be weighted)
# # a link to select a COF(COF Selection screen)

# COF Selection screen,
# # user is asked to select a course of fire(COF)
# # # user is given instructions and conditions for the COF

# user inputs results for the COF

# user is given instructions and conditions for the COF

# user is displayed skills score from results from last COF


# f = open("user_local_hist_cof.csv", "w")
# f.write(f'date,'
#         f'shot_number,'
#         f'Hit,'
#         f'score,'
#         f'time,'
#         f'target,'
#         f'hit location,'
#         f'reload\n')
# f.close()


def write_to_file_append(file_name, file_values):
    print(file_values)
    f = open(file_name, "a")
    f.write(file_values)
    f.close()


def id_user():
    name = input('Please log in with last name: ')
    with open("Users.csv", mode='r')as csv_file_user:
        csv_reader_user = csv.DictReader(csv_file_user)
        for row in csv_reader_user:
            if name in row["Last_name"]:
                print(f"{name}, it's time to get harder to kill.")
                current_user = csv_reader_user


def select_cof():
    with open("course_of_fire.csv", mode='r') as csv_file_cof:
        csv_reader_cof = csv.DictReader(csv_file_cof)
        print('Select from the following Courses of fire.\n')

        for row in csv_reader_cof:
            print(f'{row["name"]}, Drill number {row["cof_id"]}')

        print('\n')
        reader = csv.reader(open('course_of_fire.csv'))
        result = {}
        for row in reader:
            key = row[0]
            if key in result:
                # implement your duplicate row handling here
                pass
            result[key] = row[1:]
        # print(result)
        selected_cof_number = input("Which Drill number will you run?")
        # print(result[selected_cof_number])

        selected_cof_inprog = result[selected_cof_number]
        cof_name = selected_cof_inprog[0]
        cof_min_rd_count = selected_cof_inprog[1]
        cof_max_distance = selected_cof_inprog[2]
        cof_field_of_fire = selected_cof_inprog[3]
        cof_number_of_targets = selected_cof_inprog[4]
        cof_target_001_type = selected_cof_inprog[5]
        cof_target_001_positions = selected_cof_inprog[6]
        cof_target_002_type = selected_cof_inprog[7]
        cof_target_002_positions = selected_cof_inprog[8]
        cof_starting_position = selected_cof_inprog[9]
        cof_firing_positions = selected_cof_inprog[10]
        cof_starting_conditions = selected_cof_inprog[11]
        cof_reloads = selected_cof_inprog[12]
        cof_transition = selected_cof_inprog[13]
        cof_Movement = selected_cof_inprog[14]
        cof_Judgement = selected_cof_inprog[15]
        cof_failure_simulations = selected_cof_inprog[16]
        cof_scoring = selected_cof_inprog[17]
        cof_instructions = selected_cof_inprog[18]

        # break_target_location('target_location001', cof_target_001_positions)
        target_location001 = cof_target_001_positions.split("_")
        degree_from_zero = target_location001[0]
        distance_from_zero = target_location001[1]
        hight_above_zero = target_location001[2]
        facing_angle = target_location001[3]
        angle_of_rotation = target_location001[4]

        print(f"Set up your target {distance_from_zero} inchs from your firing postion")

        print("\n")
        print(f"You have selected to run Drill Number {selected_cof_number} - {cof_name}!\n")
        print("Instructions")
        print(cof_instructions)


def record_results():
    print("Enter your results!")
    # with open("user_local_hist_cof.csv", mode='r')as loc_hist:
    #     for row in loc_hist:
    #         shot_number001 = f'{row["shot_number"]}'
    f = open("user_local_hist_cof.csv", "a")
    # date, shot_number, Hit, score,time,target,hit location, reload
    record_shot_1_date = datetime.datetime.now()
    with open("user_local_hist_cof.csv", mode='r')as loc_hist:
        csv_reader = csv.DictReader(loc_hist)
        for row in csv_reader:
            shotnumber = int(row['shot_number'])
    shot_number = shotnumber + 1
    record_shot_1_hit = input('Did you hit the score zone? Y/N ')
    record_shot_1_score = input('How many points did you score? ')
    record_shot_1_time = input('Enter the time of your first shot in seconds ')
    record_shot_1_target = input("What target where you aiming at? ")
    record_shot_1_hit_location = input("Where did the shot land on the target? ")
    record_shot_1_reload = input('Did you have to reload? Y/N ')
    shot_record_line = f'\n{record_shot_1_date}, ' \
                       f'{shot_number}, ' \
                       f'{record_shot_1_hit}, ' \
                       f'{record_shot_1_score}, ' \
                       f'{record_shot_1_time},' \
                       f'{record_shot_1_target}, ' \
                       f'{record_shot_1_hit_location}, ' \
                       f'{record_shot_1_reload}'
    print(shot_record_line)
    f.write(shot_record_line)
    f.close()


# with open("user_local_hist_cof.csv", mode='r')as loc_hist:
#     csv_reader = csv.DictReader(loc_hist)
#     for row in csv_reader:
#         print(row)
#         shotnumber = int(row['shot_number'])


