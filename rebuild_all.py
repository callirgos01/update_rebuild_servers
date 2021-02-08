import os, shutil
import git

def rebuild_server(service_name, service_root ):
    root = "/usenet/setup/"
    service_name = "Sonarr"
    systemctl_service_name = "sonarr.service"

    service_root =  os.path.join(root, service_name) #"/usenet/setup/Sonarr/Sonarr-Source"
    service_source_root = os.path.join(service_root, service_name + "-Source")
    service_source_root_temp = service_source_root + "-Temp"

    source_remote_repo = "https://github.com/Sonarr/Sonarr.git"
    solution_path = service_source_root_temp + "/src/" + service_name + ".sln"
    build_script = service_source_root_temp + "/build.sh"

    print(root + " " + service_name + " " + service_root + " " + service_source_root + " " + service_source_root_temp + " " + solution_path )

    if os.path.isdir(service_source_root_temp):
        shutil.rmtree(service_source_root_temp)
    os.mkdir(service_source_root_temp)
    git.Git(service_source_root_temp).clone(source_remote_repo, service_source_root_temp)
    os.chdir(service_source_root_temp)
    #DOTNET RESTORE
    print("dotnet restore " + solution_path)
    os.system("dotnet restore " + solution_path);
    #build solution
    print("building")
    #    os.system("cd " + service_source_root_temp)
    os.system(build_script)

    #steps for rebuild server
    #1. clone repo to temp folder
    #2. copy setup/config to temp folder
    #3. build temp version
    #4. if passed / built succesfully - 
        #5. stop service.
        #6. rename temp folder to live folder

    #1. stop service
    #2. clean folder of previous build
    #3. pull latest version from git - optional: add a check if we are already on top?
    #4. dotnet restore .net project (optional)
    #5. call build script inside the service (optional)
    #6. relink the UI folder (optional)
    #7. restart service.

list_of_server_update_scripts = [ 
    "sonarr/rebuild_sonar.sh",
    "radarr/rebuild_radarr.sh" , 
    "update_plex_server/update_plex.sh", 
    "nzb_to_media/update_nzbToMedia.sh", 
    "lidarr/rebuild_lidarr.sh"
]

#for script in list_of_server_update_scripts:
#   os.system(script)
rebuild_server("","")

