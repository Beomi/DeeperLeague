import requests
import os
import json


latest_version = requests.get('https://ddragon.leagueoflegends.com/api/versions.json').json()[0]

print("Latest Version:", latest_version)

short_latest_version = '.'.join(latest_version.split('.')[:2])

champions_static = f'http://ddragon.leagueoflegends.com/cdn/{latest_version}/data/en_US/champion.json'

champions = requests.get(champions_static).json()['data']

champ_names = list(champions.keys())

json.dump(obj=champ_names, fp=open('champion_names.json', 'w'))

os.makedirs('./champions', exist_ok=True)

# loop throuigh champ names

for champ_name in champ_names:
  lower_case_champ_name = champ_name.lower()
  champ_path_opt_1 = f'https://raw.communitydragon.org/{short_latest_version}/game/assets/characters/{lower_case_champ_name}/hud/{lower_case_champ_name}_circle.png'
  champ_path_opt_2 = f'https://raw.communitydragon.org/{short_latest_version}/game/assets/characters/{lower_case_champ_name}/hud/{lower_case_champ_name}_circle_0.png'
  champ_path_opt_3 = f'https://ddragon.leagueoflegends.com/cdn/{latest_version}/img/champion/{champ_name}.png'
  if(lower_case_champ_name == 'udyr'):
    champ_path_opt_1 = 'https://raw.communitydragon.org/13.14/game/assets/characters/udyr/hud/udyr_circle_0.udyrvgu.png'

  if(lower_case_champ_name == 'ahri'):
    champ_path_opt_1 = 'https://raw.communitydragon.org/13.14/game/assets/characters/ahri/hud/ahri_circle_0.skins_ahri_asu_prepro.png'

  if(lower_case_champ_name == 'anivia'):
    champ_path_opt_1 = 'https://raw.communitydragon.org/13.14/game/assets/characters/anivia/hud/cryophoenix_circle.png'

  if(lower_case_champ_name == 'belveth'):
    champ_path_opt_1 = 'https://raw.communitydragon.org/13.14/game/assets/characters/belveth/hud/belveth_circle_0.belveth.png'

  if(lower_case_champ_name == 'blitzcrank'):
    champ_path_opt_1 = 'https://raw.communitydragon.org/13.14/game/assets/characters/blitzcrank/hud/steamgolem_circle.png'

  if(lower_case_champ_name == 'chogath'):
    champ_path_opt_1 = 'https://raw.communitydragon.org/13.14/game/assets/characters/chogath/hud/greenterror_circle.png'
  
  if(lower_case_champ_name == 'hecarim'):
    champ_path_opt_1 = 'https://raw.communitydragon.org/13.14/game/assets/characters/hecarim/hud/hecarim_circle_0.pie_c_13_6.png'

  if(lower_case_champ_name == 'ksante'):
    champ_path_opt_1 = 'https://raw.communitydragon.org/13.14/game/assets/characters/ksante/hud/ksante_circle_0.ksante.png'

  if(lower_case_champ_name == 'milio'):
    champ_path_opt_1 = 'https://raw.communitydragon.org/13.14/game/assets/characters/milio/hud/milio_circle_0.milio.png'

  if(lower_case_champ_name == 'naafiri'):
    champ_path_opt_1 = 'https://raw.communitydragon.org/13.14/game/assets/characters/naafiri/hud/naafiri_circle.naafiri.png'

  if(lower_case_champ_name == 'nilah'):
    champ_path_opt_1 = 'https://raw.communitydragon.org/13.14/game/assets/characters/nilah/hud/nilah_circle_0.nilah.png'

  if(lower_case_champ_name == 'orianna'):
    champ_path_opt_1 = 'https://raw.communitydragon.org/13.14/game/assets/characters/orianna/hud/oriana_circle.png'

  if(lower_case_champ_name == 'rammus'):
    champ_path_opt_1 = 'https://raw.communitydragon.org/13.14/game/assets/characters/rammus/hud/armordillo_circle.png'

  if(lower_case_champ_name == 'shaco'):
    champ_path_opt_1 = 'https://raw.communitydragon.org/13.14/game/assets/characters/shaco/hud/jester_circle.png'

  if(lower_case_champ_name == 'zilean'):
    champ_path_opt_1 = 'https://raw.communitydragon.org/13.14/game/assets/characters/zilean/hud/chronokeeper_circle.png'

  response = requests.get(champ_path_opt_1)
  if response.status_code != 200:
    response = requests.get(champ_path_opt_2)
  if response.status_code != 200:
    response = requests.get(champ_path_opt_3)

  if response.status_code != 200:
    print(champ_path_opt_1)
    print(champ_path_opt_2)
    print(champ_path_opt_3)
    print("failed to get champ circle for {0}".format(champ_name))
    continue

  # make a dir for the champ
  if not os.path.exists('./champions/{0}'.format(champ_name)):
    os.mkdir('./champions/{0}'.format(champ_name))

  with open('./champions/{0}/1.png'.format(champ_name), 'wb') as f:
    f.write(response.content)

  if lower_case_champ_name == 'kayn':
    assasin_image_path = 'https://raw.communitydragon.org/15.10/game/assets/characters/kayn/hud/kayn_ass_circle.png'
    response = requests.get(assasin_image_path)
    if(response.status_code != 200):
      print("Failed to get kayn assasin form image")
    else:
      with open('./champions/{0}/2.png'.format(champ_name), 'wb') as f:
        f.write(response.content)
      
      
    darkin_image_path = 'https://raw.communitydragon.org/15.10/game/assets/characters/kayn/hud/kayn_slay_circle.png'
    response = requests.get(darkin_image_path)
    if(response.status_code != 200):
      print("Failed to get kayn darkin form image")
    else:
      with open('./champions/{0}/3.png'.format(champ_name), 'wb') as f:
        f.write(response.content)
      
  if lower_case_champ_name == 'gnar':
    megagnar_path = 'https://raw.communitydragon.org/15.10/game/assets/characters/gnarbig/hud/gnarbig_circle.png'
    response = requests.get(megagnar_path)
    if(response.status_code != 200):
      print("Failed to get mega gnar form image")
    else:
      with open('./champions/{0}/2.png'.format(champ_name), 'wb') as f:
        f.write(response.content)

  if lower_case_champ_name == 'yuumi':
    yuumi_path = 'https://raw.communitydragon.org/15.10/game/assets/characters/yuumi/hud/yuumi_circle_0.png'
    response = requests.get(yuumi_path)
    if(response.status_code != 200):
      print("Failed to get yuumi form image")
    else:
      with open('./champions/{0}/2.png'.format(champ_name), 'wb') as f:
        f.write(response.content)

  print(champ_name)