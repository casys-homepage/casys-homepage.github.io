from django.db import models


class Path:
    def __init__(self):
        self.base = "/home/lab/calab_django/"
        self.contents = self.base + "core/contents/"
    def templates(self):
        return self.base + "core/templates/"
    def students(self):
        return self.contents + "students.csv"
    def members_photo_csv(self):
        return self.contents + "members_photo.csv"
    def photos_dir(self):
        return "static/img/labmembers"
    def publications(self):
        return self.contents + "publications.csv"
    def projects(self):
        return self.contents + "projects.csv"
    def papers(self):
        return self.base + "static/papers/"


class Members:
    def __init__(self, path):
        self.postdoc = []
        self.phd     = []
        self.ms      = []
        self.alumni  = []

        students_csv = open(path.students(), "r")
        for line in students_csv:
            stripped_line = line.strip()
            splitted_line = stripped_line.split(",")
            category      = splitted_line[0]
            name          = splitted_line[2]
            url           = splitted_line[3]
            if category == "postdoc":
                self.postdoc.append({"name": name, "url": url})
            elif category == "phd":
                self.phd.append({"name": name, "url": url})
            elif category == "ms":
                self.ms.append({"name": name, "url": url})
            elif category == "alumni":
                name = splitted_line[2]
                url  = splitted_line[-1]
                self.alumni.append({"name": name, "url": url})
        students_csv.close()

    def get_member_list(self):
        return self.alumni, self.postdoc, self.phd, self.ms


class Album:
    def __init__(self, path):
        self.photo_li = []

        members_photo_csv = open(path.members_photo_csv(), "r")
        for line in members_photo_csv:
            stripped_line = line.strip()
            img_path = "%s/%s" % (path.photos_dir(), stripped_line )
            year = self.get_year_from_file(stripped_line)
            elem = { "img_path" : img_path , "title" : year + " Lab Members"}
            self.photo_li.append(elem)
        members_photo_csv.close()

    def get_year_from_file(self, filename):
        filename = filename.replace("labmembers_", "")
        filename = filename.replace(".jpg", "")
        filename = filename.replace("unknown0", "")
        filename = filename.replace("unknown1", "")
        return filename

    def get_photo_list(self):
        return self.photo_li


class Publications:
    def __init__(self, path):
        publications_csv = open(path.publications(), "r")

        self.all_pub = []
        self.international_conference  = []
        self.international_journal     = []
        self.domestic_conference       = []
        self.domestic_journal          = []

        curr_year = None
        category_check = []

        for line in publications_csv:
            if not line[0] == "#":
                stripped_line = line.strip()
                splitted_line = stripped_line.split("$")
                category = splitted_line[0]
                year = splitted_line[1]
                paper = splitted_line[2]
                url = splitted_line[3]
                print_year = False
                if curr_year != year:
                    curr_year = year
                    print_year = True
                    category_check = []
                    category_check.append(category)

                self.all_pub.append( \
                    {"paper": paper, "url": url, "year": year, "print_year": print_year}
                )
                
                if print_year is False and category not in category_check:
                    print_year = True
                    category_check.append(category)

                if category == "international_conference":
                    self.international_conference.append(\
                            {"paper": paper, "url": url, "year": year, "print_year": print_year}
                            )
                elif category == "international_journal":
                    self.international_journal.append(\
                            {"paper": paper, "url": url, "year": year, "print_year": print_year}
                            )
                elif category == "domestic_conference":
                    self.domestic_conference.append(\
                            {"paper": paper, "url": url, "year": year, "print_year": print_year}
                            )
                elif category == "domestic_journal":
                    self.domestic_journal.append(\
                            {"paper": paper, "url": url, "year": year, "print_year": print_year}
                            )


        publications_csv.close()

    def get_all(self):
        return self.all_pub

    def get_international_conference(self):
        return self.international_conference

    def get_international_journal(self):
        return self.international_journal

    def get_domestic_conference(self):
        return self.domestic_conference

    def get_domestic_journal(self):
        return self.domestic_journal


class Projects:
    def __init__(self, path):
        projects_csv = open(path.projects(), "r")

        self.ongoing_projects = []
        self.past_projects    = []

        for line in projects_csv:
            line = line.strip()
            splitted_line = line.split("$")

            project_category    = splitted_line[0]
            project_period      = splitted_line[1]
            project_name        = splitted_line[2]
            project_affiliation = splitted_line[3]

            if project_category == "ongoing":
                self.ongoing_projects.append({"project_period": project_period,
                                              "project_name": project_name,
                                              "project_affiliation": project_affiliation})
            elif project_category == "past":
                self.past_projects.append({"project_period": project_period,
                                           "project_name": project_name,
                                           "project_affiliation": project_affiliation})

        projects_csv.close()

    def get_past_projects(self):
        return self.past_projects

    def get_ongoing_projects(self):
        return self.ongoing_projects
