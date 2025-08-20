# Reflection: Grazioso Salvare Dashboard

## How do you write programs that are maintainable, readable, and adaptable?

To write programs that are maintainable, readable, and adaptable, I focused on clean coding practices, consistent naming conventions, and modular design. For example, the CRUD Python module developed in Project One encapsulates all database operations inside a dedicated class [AnimalShelter](https://github.com/Aqbah/CS-340/blob/main/Web%20Dashboard/AnimalShelter.py). This separation of concerns meant that in Project Two, I could easily reuse the module without rewriting database logic. The main advantage of working this way is that the database interface is abstracted: if MongoDB changes or if Grazioso Salvare switches to a different database, I would only need to modify the CRUD module, not the entire dashboard.
This module could also be reused in the future for other dashboards, APIs, or command-line tools that need to interact with the same data, making it both adaptable and extensible.

## How do you approach a problem as a computer scientist?

My approach to this project started with understanding the client requirements and then mapping them into the MVC (Model-View-Controller) design pattern. For example:

- The Model was the [MongoDB](https://www.mongodb.com/) database connected through the CRUD module.

- The View was the interactive dashboard widgets created with [Dash](https://dash.plotly.com/).

- The Controller was the callback logic linking filters, charts, and the data table.

Compared to other coursework, this project required me to think more like a systems integrator rather than solving isolated coding tasks. I had to design with the end-user in mind, ensuring the interface was intuitive while the backend queries were efficient.
In the future, I would apply strategies like modular coding, incremental testing, and client-driven design when creating databases and dashboards. This ensures that requirements are met while the code remains flexible for future updates.

## What do computer scientists do, and why does it matter?

Computer scientists solve real-world problems by designing and building software that helps organizations make better decisions and operate more efficiently. In this project, my work directly helps Grazioso Salvare identify and categorize dogs suitable for search-and-rescue training. By providing filtering, visualization, and mapping tools, the dashboard reduces the time and effort required for staff to analyze shelter data.
This matters because technology like this allows mission-driven organizations to be more effective in their work—in this case, saving lives through faster deployment of trained rescue dogs. More broadly, computer scientists create the tools and systems that power industries, drive innovation, and ultimately improve people’s lives.
