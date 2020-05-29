import csv
import datetime


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


def break_target_location(target_name_num, location):
    print(target_name_num)
    target_name_num = location.split("_")
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


def write_to_file_append(file_name, file_values):
    print(file_values)
    f = open(file_name, "a")
    f.write(file_values)
    f.close()


# cof_id,name,min_rd_count,max_distance,field of fire,number_of_targets,target_001_type,target_001_positions,target_002_type,target_002_positions,starting_position,firing positions,starting conditions,reloads,transition,Movement,Judgement,failure simulations,scoring,instructions


cof_selected = {'cof_id': 1,
                'name': 'F.A.S.T Drill',
                'min_rd_count': 6,
                # need to define the values used, i vote millimeters and we convert based on user preference
                'max_distance': '7 yards',
                # we could define this based of of positions relative to shooting position
                'field of fire': 180,
                'number_of_targets': 2,
                # how do we add if we have a COF with 15 targets?
                'target_001_type': '3x5',
                # Target location
                # Zero = 0_0_0_0_0 is the center of the starting postion at ground level
                # formula is (degree from 0 with 360 , distance from 0 in inchs, hight to top target top from 0 elevation, directions of relitive to 0 360, degree of rotation)
                # 360_252_70_180_0
                'target_001_positions': '360_252_70_180_0',
                'target_002_type': 'circle 8in',
                'target_002_positions': '360_252_60_180_0',
                'starting_position': 'holstered',
                'firing positions': 1,
                # all subsequent firing positions are based in relation to firing position 1 assumed to be 0_0_0_0_0
                # need to be able to add more firing positions
                'Firing_pos_002': '90_72_0_360_0',
                # based off a list
                'starting conditions': 'loaded_chambered_Y_1',
                # only define if planned or reload is required. we then compare this to the results to look for none planned reloads
                'reloads': 1,
                # ref to handgun: primary to support, support to primary or to other weapon systems
                'transition': 0,
                # base of the number of firing positions and the distance between them can calc movement speed/ time
                'Movement': 0,
                # for shoot/ no shoot drills
                'Judgement': 0,
                # set value based off list of known drills spilt after drill is value per fail type
                'failure simulations': 0,
                # based off of a list, 1 = only hits count for 1 point
                'scoring': 1,
                'instructions': "You will start with your weapon holstered and chambered, with 1(one) round in the magizine. You will have a second magizine loaded with 4 (four) rounds in a carrier. On the command to fire you will 1. Draw from concealment, 2. fire 2 rounds on target 1, 3. reload - slide-lock, 4. fire 4 on target 2. Then make clear and holster your weapon"}


shot_001 = {'date': '2020-05-22 21:13:06.035995',
            'shot_number': 1,
            'Hit': 'Y',
            # score will have to be calculated off cof_selected['scoring'] and or off the target table and hit Y/N
            'score': cof_selected['scoring'],
            'time': 1.2,
            'target': cof_selected['target_001_type'],
            # I am assuming base off a top left 0, 0 and one inch left, down
            'hit location': '2x4',
            # set to true if a reload happened after this shot
            'reload': False}

shot_002 = {'date': '2020-05-22 21:43:00.237648',
            'shot_number': 2,
            'Hit':  'Y',
            'score': cof_selected['scoring'],
            'time': 1.5,
            'target': cof_selected['target_001_type'],
            'hit location': '1x4',
            'reload': False}

shot_003 = {'date': '2020-05-22 21:44:06.877975',
            'shot_number': 3,
            'Hit': 'Y',
            'score': cof_selected['scoring'],
            'time': 2.1,
            'target': cof_selected['target_002_type'],
            'hit location': 0,
            'reload': True}

shot_004 = {'date': '2020-05-22 21:46:05.028365',
            'shot_number': 4,
            'Hit': 'Y',
            'score': cof_selected['scoring'],
            'time': 2.2,
            'target': cof_selected['target_002_type'],
            'hit location': '4x5',
            'reload': False}

shot_005 = {'date': '2020-05-22 21:46:05.028365',
            'shot_number': 5,
            'Hit': 'Y',
            'score': cof_selected['scoring'],
            'time': 2.4,
            'target': cof_selected['target_002_type'],
            'hit location': '3x3',
            'reload': False}

shot_006 = {'date': '2020-05-22 21:46:05.028365',
            'shot_number': 6,
            'Hit': 'Y',
            'score': cof_selected['scoring'],
            'time': 2.6,
            'target': cof_selected['target_002_type'],
            'hit location': '3x4',
            'reload': False}

for key, value in cof_selected.items():
    if '_positions' in key:
        # print(value)
        break_target_location(f'{key}', value)
    if 'number_of_targets' in key:
        print(f'There are {value} Targets')


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

# "distance between targets"

# Baseline skills test
# Draw from holster
# Reloading (can break down)
# Recoil management (controlled pairs, groups on same target)
# Target transition (rate that user can engage another target)
# Accuracy
# Judgement (shoot/ no shoot)
# Movement (can break down)
# Shooting positions (can break down)
# Support hand (can break down)

# Categories
# 1. split = Draw from holster (buzzer to round 1)
# 2. split = Recoil management (round 1 to round 2)
# 3. split = Reloading (Round 2 to round 3)
# 4. split = Recoil management (round 3 to round 6)


Core_skills_time_on_target_holstered = 0
Core_skills_time_on_target_low_ready = 0
Core_skills_time_on_target_high_ready = 0
Core_skills_time_on_target_tabled = 0
Core_skills_time_on_target_grounded = 0
Core_skills_combat_accuracy = 0
Core_skills_Recoil_management = 0
Core_skills_Reload_slide_lock = 0
Core_skills_target_tanstion = 0



# each function should log a record of the date, time, cof, skill, and value in a user history

def list_splits():
    # takes all shots in results and creates 1 value per the difference between times
    print('Split')


# mock data from list_splits()
split_001 = 1.2
split_002 = 1.5
split_003 = 2.1
split_004 = 2.2
split_005 = 2.4
split_006 = 2.6
split_007 = 0
split_008 = 0


def reload_slidelock():
    # looks in the results string for where a reload was done and assigned the split time after that as the value
    # this should cycle through all results
    if shot_003['reload'] == True:
        Core_skills_Reload_slide_lock = split_004
    print(f'Reload took {split_004} seconds')


def target_tanstion():
    print('target_tanstion')
    if cof_selected['number_of_targets'] > 1:
        target001 = shot_001['target']
        if shot_003['target'] == target001:
            print('same')
        else:
            Core_skills_target_tanstion = shot_003
    # add logic to handle if  reload is present


def ontarget_from():
    if cof_selected['starting_position'] == 'holstered':
        Core_skills_time_on_target_holstered = split_001
    elif cof_selected['starting_position'] == 'Low Ready':
        Core_skills_time_on_target_low_ready = split_001
    elif cof_selected['starting_position'] == 'High Ready':
        Core_skills_time_on_target_high_ready = split_001
    elif cof_selected['starting_position'] == 'tabled':
        Core_skills_time_on_target_tabled = split_001
    elif cof_selected['starting_position'] == 'grounded':
        Core_skills_time_on_target_grounded = split_001
    # add from a reload
    print(f"User started {cof_selected['starting_position']} and took {split_001} seconds to hit the target")


# ontarget_from()
target_tanstion()

