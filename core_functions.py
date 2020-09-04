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

# ###########################################     SKills breakdown, start   ############################################

Core_skills_time_on_target_holstered = 0
Core_skills_time_on_target_low_ready = 0
Core_skills_time_on_target_high_ready = 0
Core_skills_time_on_target_tabled = 0
Core_skills_time_on_target_grounded = 0
# All time on target are the score of the first shot group by 'starting_position' in COF

Core_skills_combat_accuracy_3 = 0
Core_skills_combat_accuracy_5 = 0
Core_skills_combat_accuracy_7 = 0
Core_skills_combat_accuracy_10 = 0
Core_skills_combat_accuracy_15 = 0
Core_skills_combat_accuracy_20 = 0
# area of target divided time
# TODO Create an equation to represent speed vs accuracy where there is a correlation between how big the target is on the time it takes to hit it. 8in/100%/2.1 second, 6in/100%/4 second

Core_skills_precision = 0
# TODO Create an equation to represent of group size non timed ????

Core_skills_Recoil_management = 0
# split between shots on the same target

Core_skills_Reload_slide_lock = 0
# spit time where a slide lock reload happens - (if target is same as last shot fired - average of Recoil_management. If the target is different from the last target fired on - the average of Core_skills_target_transition

Core_skills_Reload_tactical = 0
# spit time where a tactical lock reload happens - (if target is same as last shot fired - average of Recoil_management. If the target is different from the last target fired on - the average of Core_skills_target_transition

Core_skills_Reload_movement = 0
# time moving from one shooting position to the next - the average of time_on_target of high and low ready

Core_skills_target_transition = 0
# split where target is different from the last target fired on

Core_skills_Judgement_no_shoot = 0
# TODO. If a COF has a target defined as a 'Judgement_no_shoot' target any shots to that target will have a flag/ point added per shot

Core_skills_Judgement_obscured = 0
# TODO. If a target in a COF is defined as 'Judgement_obscured' any shot to the obscured area will have a flag/ point added per shot and set any shot to the target as a miss

core_skill_clear_failure = 0
# Split minus the average of historic time_on_target for high and low ready = core_skill_clear_failure
# If a failure occurs during a COF the split - the average of historic time_on_target of high and low ready is set as clear_failure

core_skill_support_hand = 0


# each function should log a record of the date, time, cof, skill, and value in a user history
# TODO define the historic average for each core skill (may use average of last results within 10% variance of each other to account for change in baseline of core skill)

# ###########################################     SKills breakdown, end   ############################################



