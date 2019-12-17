import json
import operator

art_works = json.load(open('Artworks.json'))
collections = json.load(open('Artworks.json'))

artworks = {}

for collection in collections:   
    # print('1', collection)
    if collection["Artist"] in artworks:
        artworks[collection["Artist"]] += 1
    else:  
        artworks[collection["Artist"]] = 1
        # print('2', artworks)

print(artworks) 

artist_dict = {}
nationality_dict = {}
gender_dict = {'Male': 0, 'Female': 0}
medium_dict = {}
title_dict = {'Manhattan': 0, 'New York': 0}


for art_work in art_works:
    # start to count artists
    artists = art_work.get('Artist')
    for art in artists:
        if not artist_dict.get(art):
            artist_dict[art] = 1
        else:
            artist_dict[art] = artist_dict.get(art) + 1
    # end count artists

    # start to count Nationalities
    nationalities = art_work.get('Nationality')
    for nationality in nationalities:
        if not nationality_dict.get(nationality):
            nationality_dict[nationality] = 1
        else:
            nationality_dict[nationality] = nationality_dict.get(nationality) + 1
    # end count Nationalities

    # start to count Gender
    genders = art_work.get('Gender')
    for gender in genders:
        if gender == 'Male':
            gender_dict['Male'] = gender_dict.get('Male') + 1
        elif gender == 'Female':
            gender_dict['Female'] = gender_dict.get('Female') + 1
    # end count Gender

    # start to count medium
    medium = art_work.get('Medium')
    if not medium_dict.get(medium):
        medium_dict[medium] = 1
    else:
        medium_dict[medium] = medium_dict.get(medium) + 1
    # end to count medium

    # start to count title
    title = art_work.get('Title')
    if 'Manhattan' in title:
        title_dict['Manhattan'] = title_dict.get('Manhattan') + 1
    elif 'New York' in title:
        title_dict['New York'] = title_dict.get('New York') + 1
    # end count title


print('>> total artist count is {}, and [{}] \n'.format(len(artist_dict), artist_dict))
print('>> Nationality is {} \n'.format(nationality_dict))
print('>> Gender is {} \n'.format(gender_dict))
print('>> Title is {} \n'.format(title_dict))

# medium_dict is tooooooo big,so print with iterator
print('Medium count as below:')
for each in artist_dict.items():
    print(each)

artist_sorted_list = sorted(artist_dict.items(), key=lambda x: x[1], reverse=True)
print('Top 10 in artist_dict is >> {} \n'.format(artist_sorted_list[:10]))

nationality_sorted_list = sorted(nationality_dict.items(), key=lambda x: x[1], reverse=True)
print('Top 10 in nationality_dict is >> {} \n'.format(nationality_sorted_list[:10]))

medium_sorted_list = sorted(medium_dict.items(), key=lambda x: x[1], reverse=True)
print('Top 10 in medium_dict is >> {} \n'.format(medium_sorted_list[:10]))

data = px.data.gapminder()
x2 = list(title_dict.keys())
y2 = list(title_dict.values())
fig = px.bar(data, x=x2, y=y2,
             hover_data=[x2, y2], color=y2,
             labels={'number of artworks':y2}, height=400)
fig.show()


labels = ['Manhattan','New York']
values = [133, 2344]

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()
