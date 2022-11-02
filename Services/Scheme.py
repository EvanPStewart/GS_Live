'''Evan Pavetto-Stewart'''
'''Scheme'''


import json
import os
import shutil


class scheme:

    def create_scheme():

        '''Allows a user to create a scheme'''
        
        '''Scheme Name'''
        name_in = input('Name: ')

        invalid_file_name = ['<','>',':','''"''','/',R'\'','|','?','*'] # R'\'' second quote?
        invalid = False # Invalid file name indicators
        invalid2 = True

        '''Check for an invalid file name and replace spaces with _'s in file name'''
        while(invalid2 == True):
            if name_in == '':
                enter_file_name_message = '''No file name detected.
                Enter file name: '''
                name_in = input(enter_file_name_message)

            for name_index in range(len(name_in)):

                for invalid_index in range(len(invalid_file_name)):

                    if(name_in[name_index] == invalid_file_name[invalid_index]):
                        print(invalid_file_name[invalid_index] + ' can not be used in a file name')
                        invalid = True
                        break
                
                if invalid == True:
                    break

                if name_in[name_index] == ' ':
                    name_in = name_in.replace(name_in[name_index],'_')
            
            if invalid == False:
                break

            if invalid == True:
                name_in = input('Enter file name: ')
                invalid = False
                
        
        '''Nose-axis'''
        nose_axis = input('Nose-axis: ')

        '''Check for invalid nose-axis input''' 
    
        nose_axis_input_message = '''Please input either x, y, or z 
        Nose-axis: '''

        while (nose_axis != 'x' and nose_axis != 'y' and nose_axis != 'z'):
            nose_axis = input(nose_axis_input_message) 
        
        '''Stages'''
        try:

            stages = int(input('Number of stages: '))
            stages_message = '''The number of stages must be greater than one
            Number of stages: '''

            while(stages < 1):
                stages = int(input(stages_message))
        
        except ValueError:
            stages_message2 = '''The number of stages must be an integer
            Number of stages: '''
            stages = int(input(stages_message2)) # How do I make it so that there are infinite tries to put in a integer. If I try to do a while loop it raises an UnboundLocalError

        '''Cd'''
        Cd = []
        Cd_message = '''Cd can not be less than 0
        Cd: '''

        for Cd_index in range(stages):
            Cd_in = float(input('Cd stage ' + str(Cd_index + 1) + ':')) 
            while (Cd_in < 0):
                Cd_in = float(input(Cd_message))
            Cd.append(Cd_in)

        '''a_f'''
        a_f = []
        a_f_message = '''a_f can not be less than 0
        a_f: '''

        for a_f_index in range(stages):
            a_f_in = float(input('a_f stage' + str(a_f_index + 1) + ':'))
            while (a_f_in < 0):
                a_f_in = float(input(a_f_message))
            a_f.append(a_f_in)

        '''m_i'''
        m_i = []
        m_i_message = '''m_i can not be less than 0
        m_i: '''

        for m_i_index in range(stages):
            m_i_in = float(input('m_i stage ' + str(m_i_index + 1) + ':'))
            while (m_i_in < 0):
                m_i_in = float(input(m_i_message))
            m_i.append(m_i_in)

        '''m_f'''
        m_f = []
        m_f_message = '''m_f can not be less than 0
        m_f: '''

        for m_f_index in range(stages):
            m_f_in = float(input('m_f stage ' + str(m_f_index + 1) + ':'))
            while (m_f_in < 0):
                m_f_in = float(input(m_f_message))
            m_f.append(m_f_in)

        '''isp'''
        isp = []
        isp_message = '''isp can not be less than 0
        isp: '''

        for isp_index in range(stages):
            isp_in = float(input('isp stages ' + str(isp_index + 1) + ':'))
            while (isp_in < 0):
                isp_in = float(input(isp_message))
            isp.append(isp_in)

        '''Accel L Mode'''
        accel_L_mode = input('Accel L Mode: ')    

        '''Accel H Mode'''
        accel_H_mode = input('Accel H Mode: ')

        '''Gyro Mode'''
        gyro_mode = input('Gyro Mode: ')

        '''Mag Mode'''
        mag_mode = input('Mag Mode: ')
           
        '''Bar Mode'''
        bar_mode = input('Bar Mode: ')

        '''Therm Mode'''
        therm_mode = input('Therm Mode: ')        

        '''Notes'''
        notes = input('Notes: ')

        '''Create Scheme and Filepath'''

        created_scheme = {'name':name_in,'nose-axis':nose_axis,'stages':stages,'cd':Cd,'a_f':a_f,'m_i':m_f,'m_f':m_f,'isp':isp,'accel L mode':accel_L_mode,'accel H mode':accel_H_mode,'gyro mode':gyro_mode,'mag mode':mag_mode,'bar mode':bar_mode,'therm mode':therm_mode,'notes':notes}

        scheme_json = json.dumps(created_scheme,indent=4)

        scheme_filepath = 'c:/Users/Evan/OneDrive/Documents/EmbryRiddle/Python Coding Projects/' + name_in

        '''Save Scheme to Filepath'''

        try:

            with open(scheme_filepath,'w') as outfile:
                outfile.write(scheme_json)
        
        except FileNotFoundError:
            print('File not found')
        
        except FileExistsError:
            print('File already exists')

    #create_scheme()

    def copy_rename_scheme(scheme_filepath):

        '''Makes a copy of the scheme create in create_scheme(). Only the scheme name can be edited'''

        try:

            new_name = input('Name of scheme copy: ')
            new_path = 'c:/Users/Evan/OneDrive/Documents/EmbryRiddle/Python Coding Projects/' + new_name

            shutil.copyfile(scheme_filepath, new_path) # copy scheme

            open_scheme_copy = open(new_path, 'r+')
            scheme_copy = json.load(open_scheme_copy)

            scheme_copy['name'] = new_name # edit the name in the copy

            '''Check for an invalid file name and replace spaces with _'s in file name'''

            invalid_file_name = ['<','>',':','''"''','/',R'\'','|','?','*'] # R'\'' second quote?
            invalid = False # Invalid file name indicators
            invalid2 = True

            while(invalid2 == True):
                if new_name == '':
                    enter_file_name_message = '''No file name detected.
                    Enter file name: '''
                    new_name = input(enter_file_name_message)

                for name_index in range(len(new_name)):

                    for invalid_index in range(len(invalid_file_name)):

                        if(new_name[name_index] == invalid_file_name[invalid_index]):
                            print(invalid_file_name[invalid_index] + ' can not be used in a file name')
                            invalid = True
                            break
                    
                    if invalid == True:
                        break

                    if new_name[name_index] == ' ':
                        new_name = new_name.replace(new_name[name_index],'_')
                
                if invalid == False:
                    break

                if invalid == True:
                    new_name = input('Enter file name: ')
                    invalid = False
            
            open_scheme_copy.close()
            
            open_scheme_copy2 = open(new_path, 'w')

            open_scheme_copy2.write(json.dumps(scheme_copy,indent=4)) # overwrite copy name

            open_scheme_copy2.close()

        except IOError:
            print('File not found. Please check the path.')
        finally:
            print('Exit')

    #copy_rename_scheme('c:/Users/Evan/OneDrive/Documents/EmbryRiddle/Python Coding Projects/test_e')

    def edit_scheme(scheme_filepath):

        '''Creates a copy of the scheme and allows the user to edit any value in the scheme copy'''
        '''If the user makes a mistake while editing any part of the scheme, they must say no to the finished editing question and start again from the beginning'''

        scheme.copy_rename_scheme(scheme_filepath) 

        open_scheme_copy = open(scheme_filepath, 'r+')
        scheme_copy = json.load(open_scheme_copy)

        editing = True # This is true while the user is editing the scheme. It becomes false when the user incicated they are done editing the scheme

        while(editing == True):

            scheme_edit_message = '''What do you want to edit?
            A: Nose-axis
            B: Number of stages
            C: Accel L Mode
            D: Accel H Mode
            E: Gyro Mode
            F: Mag Mode
            G: Bar Mode
            H: Therm Mode
            I: Notes
            
            '''

            scheme_edit = input(scheme_edit_message)

            if scheme_edit == 'A':

                '''Edit Nose-axis'''
                new_nose_axis = input('New Nose-axis: ')

                '''Check for invalid nose-axis input''' 
        
                new_nose_axis_input_message = '''Please input either x, y, or z 
                Nose-axis: '''

                while (new_nose_axis != 'x' and new_nose_axis != 'y' and new_nose_axis != 'z'):
                    new_nose_axis = input(new_nose_axis_input_message) 

                scheme_copy['nose-axis'] = new_nose_axis # Replaces nose-axis in scheme with new nose axis value

            if scheme_edit == 'B':

                '''Edit Stages'''

                # If the user wants to add stages and leave the previously created stages unchanged, they would have to reenter the data for those stages
                # If the user wants to edit the data for one stage, they would have to reenter the data for the other stages

                try:

                    new_stages = int(input(' New number of stages: '))
                    new_stages_message = '''The new number of stages must be greater than one
                    New number of stages: '''

                    while(new_stages < 1):
                        new_stages = int(input(new_stages_message))
                
                except ValueError:
                    new_stages_message2 = '''The new number of stages must be an integer
                    New number of stages: '''
                    new_stages = int(input(new_stages_message2)) # How do I make it so that there are infinite tries to put in a integer. If I try to do a while loop it raises an UnboundLocalError

                scheme_copy['stages'] = new_stages # Replaces number of stages in scheme with new number of stages value

                '''Edit Cd'''
                new_Cd = []
                new_Cd_message = '''New Cd can not be less than 0
                Cd: '''

                for Cd_index in range(new_stages):
                    new_Cd_in = float(input('New Cd stage ' + str(Cd_index + 1) + ':')) 
                    while (new_Cd_in < 0):
                        new_Cd_in = float(input(new_Cd_message))
                    new_Cd.append(new_Cd_in)

                scheme_copy['cd'] = new_Cd # Replaces Cd in scheme with Cd value

                '''Edit a_f'''
                new_a_f = []
                new_a_f_message = '''New a_f can not be less than 0
                a_f: '''

                for a_f_index in range(new_stages):
                    new_a_f_in = float(input('New a_f stage' + str(a_f_index + 1) + ':'))
                    while (new_a_f_in < 0):
                        new_a_f_in = float(input(new_a_f_message))
                    new_a_f.append(new_a_f_in)

                scheme_copy['a_f'] = new_a_f # Replaces a_f in scheme with a_f value

                '''Edit m_i'''
                new_m_i = []
                new_m_i_message = '''New m_i can not be less than 0
                m_i: '''

                for m_i_index in range(new_stages):
                    new_m_i_in = float(input('New m_i stage ' + str(m_i_index + 1) + ':'))
                    while (new_m_i_in < 0):
                        new_m_i_in = float(input(new_m_i_message))
                    new_m_i.append(new_m_i_in)

                scheme_copy['m_i'] = new_m_i # Replaces m_i in scheme with m_i value

                '''Edit m_f'''
                new_m_f = []
                new_m_f_message = '''New m_f can not be less than 0
                m_f: '''

                for m_f_index in range(new_stages):
                    new_m_f_in = float(input('New m_f stage ' + str(m_f_index + 1) + ':'))
                    while (new_m_f_in < 0):
                        new_m_f_in = float(input(new_m_f_message))
                    new_m_f.append(new_m_f_in)

                scheme_copy['m_f'] = new_m_f # Replaces m_f in scheme with m_f value

                '''Edit isp'''
                new_isp = []
                new_isp_message = '''New isp can not be less than 0
                isp: '''

                for isp_index in range(new_stages):
                    new_isp_in = float(input('New isp stages ' + str(isp_index + 1) + ':'))
                    while (new_isp_in < 0):
                        new_isp_in = float(input(new_isp_message))
                    new_isp.append(new_isp_in)

                scheme_copy['isp'] = new_isp # Replaces isp in scheme with isp value

            if scheme_edit == 'C':
                
                '''Edit Accel L Mode'''
                new_accel_L_mode = input('New Accel L Mode: ')
                scheme_copy['accel_L_mode'] = new_accel_L_mode # Replaces Accel L Mode in scheme with Accel L Mode value

            if scheme_edit == 'D':

                '''Edit Accel H Mode'''
                new_accel_H_mode = input('New Accel H Mode: ')
                scheme_copy['accel_H_mode'] = new_accel_H_mode # Replaces Accel H Mode in scheme with Accel H Mode value

            if scheme_edit == 'E':

                '''Edit Gyro Mode'''
                new_gyro_mode = input('New Gyro Mode: ')
                scheme_copy['gyro mode'] = new_gyro_mode # Replaces Gyro Mode in scheme with Gyro Mode value

            if scheme_edit == 'F':

                '''Edit Mag Mode'''
                new_mag_mode = input('New Mag Mode: ')
                scheme_copy['mag mode'] = new_mag_mode # Replaces Mag Mode in scheme with Mag Mode value

            if scheme_edit == 'G':

                '''Edit Bar Mode'''
                new_bar_mode = input('New Bar Mode: ')
                scheme_copy['Bar mode'] = new_bar_mode # Replaces Bar Mode in scheme with Bar Mode value

            if scheme_edit == 'H':

                '''Edit Therm Mode'''
                new_therm_mode = input('New Therm Mode: ')
                scheme_copy['therm mode'] = new_therm_mode # Replaces Therm Mode in scheme with Therm Mode value
            
            if scheme_edit == 'I':

                '''Edit Notes'''
                new_gyro_mode = input('New Gyro Mode: ')
                scheme_copy['gyro mode'] = new_gyro_mode # Replaces Gyro Mode in scheme with Gyro Mode value

            '''Asks the user for another input if the first input was not valid'''

            if scheme_edit != 'A' and scheme_edit != 'B' and scheme_edit != 'C' and scheme_edit != 'D' and scheme_edit != 'E' and scheme_edit != 'F' and scheme_edit != 'G' and scheme_edit != 'H' and scheme_edit != 'I':

                valid_input = False

                scheme_edit_message2 = '''Please enter either A, B, C, D, E, F, G, H, or I
                A: Nose-axis
                B: Number of stages
                C: Accel L Mode
                D: Accel H Mode
                E: Gyro Mode
                F: Mag Mode
                G: Bar Mode
                H: Therm Mode
                I: Notes
                
                '''

                while(valid_input == False):

                    scheme_edit = input(scheme_edit_message2)

                    if(scheme_edit == 'A' or scheme_edit == 'B' or scheme_edit == 'C' or scheme_edit == 'D' or scheme_edit == 'E' or scheme_edit == 'F' or scheme_edit == 'G' or scheme_edit == 'H' or scheme_edit == 'I'):

                        valid_input = True

            finished_editing = input('Finished editing? (yes/no) ')

            if finished_editing == 'yes':

                editing = False # if yes, break out of editing while loop

            '''If invalid finished_editing input'''

            if finished_editing != 'yes' and finished_editing != 'no':

                valid_finished_editing = False
                finished_editing_message = '''Please enter yes or no
                Finished editing (y/n) '''

                while(valid_finished_editing == False):

                    finished_editing = input(finished_editing_message)

                    if finished_editing == 'yes' or finished_editing == 'no':

                        valid_finished_editing = True

                if finished_editing == 'yes':

                    editing = False # if yes, break out of editing while loop

        open_scheme_copy.close()
            
        open_scheme_copy2 = open(scheme_filepath, 'w')

        open_scheme_copy2.write(json.dumps(scheme_copy,indent=4)) # overwrite copy data

        open_scheme_copy2.close()

    #edit_scheme('c:/Users/Evan/OneDrive/Documents/EmbryRiddle/Python Coding Projects/test_e')

    def delete_scheme(scheme_filepath):
        '''Deletes a selected scheme but can also delete any file'''
        try:
            os.remove(scheme_filepath)

        except IOError:
            print("File not found. Please check the path.")

    #delete_scheme()

