import requests
import pygal

# ask user for programming language to search for
# saves starred_repos.svg - graph of repositories with the most stars
language = input("Enter programming language to search: ")
language = language.lower()

# make API call and store response
url = "https://api.github.com/search/repositories?q=language:" + language + "&sort=stars"
r = requests.get(url)

response_dict = r.json()

print("Total repositories: ", response_dict["total_count"])

repo_dicts = response_dict["items"]

names = []
plot_dicts = []

for repo_dict in repo_dicts:
    names.append(repo_dict["name"])

    plot_dict = {
       "value": repo_dict["stargazers_count"],
       "label": repo_dict["description"],
    }

    plot_dicts.append(plot_dict)

# make a bar graph
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.width = 1000

chart = pygal.Bar(my_config)
chart.title = "GitHub\'s Most Starred " + language.capitalize() + " Projects"
chart.x_labels = names
chart.add("", plot_dicts)
chart.render_to_file('starred_repos.svg')
print("Graph saved to starred_repos.svg")