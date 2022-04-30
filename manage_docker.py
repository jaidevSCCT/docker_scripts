import subprocess


class ManageDocker:
    @classmethod
    def list_all_images(cls):
        """
        list_all_images runs docker image command and return list of docker images in
        dictionary format
        It returns formatted output as image id , repo , tag and size.
        """
        image_format = {'Image ID': [], 'Repository': [], 'Tag': [], 'Size': []}
        try:
            images_cmd_out = subprocess.run(["docker images --format \"table {{.ID}}:{{.Repository}}:{{.Tag}}:{{"
                                             ".Size}}\""], shell=True, check=True, stdout=subprocess.PIPE)
            images_cmd_str = images_cmd_out.stdout.decode('utf-8')
            images_str_list = images_cmd_str.splitlines()
            for value in images_str_list:
                images_per_line = value.split(':')
                image_format['Image ID'].append(images_per_line[0])
                image_format['Repository'].append(images_per_line[1])
                image_format['Tag'].append(images_per_line[2])
                image_format['Size'].append(images_per_line[3])

        except subprocess.CalledProcessError as e:
            print(e.output)
        return image_format

    @classmethod
    def list_all_containers(cls):
        """
        list_all_containers runs docker ps command and return list of containers
        in dictionary format
        It returns formatted output as image id , repo , tag and size.
        """
        container_format = {'Container ID': [], 'Image': [], 'Names': []}
        try:
            container_cmd_out = subprocess.run(["docker ps --format \"table {{.ID}}:{{.Image}}:{{.Names}}\""]
                                               , shell=True, check=True, stdout=subprocess.PIPE)
            container_cmd_str = container_cmd_out.stdout.decode('utf-8')
            container_str_list = container_cmd_str.splitlines()
            for value in container_str_list:
                container_per_line = value.split(':')
                container_format['Container ID'].append(container_per_line[0])
                container_format['Image'].append(container_per_line[1])
                container_format['Names'].append(container_per_line[2])
        except subprocess.CalledProcessError as e:
            print(e.output)
        return container_format

    @classmethod
    def search_containers(cls, search_str: str):
        """
        search_containers : returns container information running of searched string
        :return:
        """
        try:
            subprocess.run(["docker ps -f name=%s" % search_str], shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(e.output)

    @classmethod
    def input_parser(cls):
        import pandas as pd
        user_input = ''
        # to remove syntax warning SyntaxWarning: "is" with a literal.
        input_list = ['1', '2', '3', '4', 'q', '#']
        input_print = ["{1} - List all images present in the system",
                       "{2} - List all container present in the system",
                       "{3} - Search docker container if present",
                       "{4} - Check status of all running container",
                       "{q} - Exit the app"]
        print(*input_print, sep='\n')

        while user_input != input_list[4]:
            user_input = input("Enter the number (press \'q\' to quit or \'#\' to see the menu): ")
            # if user_input is '1': # gives syntax warning with literals
            if user_input is input_list[0]:
                out_res = cls.list_all_images()
                out_df = pd.DataFrame(out_res)
                print(out_df)
            elif user_input is input_list[1]:
                out_res = cls.list_all_containers()
                out_df = pd.DataFrame(out_res)
                print(out_df)
            elif user_input is input_list[2]:
                search_str = input('Enter the string to search: ')
                cls.search_containers(search_str)
            elif user_input is input_list[5]:
                print(*input_print, sep='\n')
            elif user_input is input_list[4]:
                print('Exiting..............')
            else:
                print("invalid input")


if __name__ == '__main__':
    ManageDocker.input_parser()
