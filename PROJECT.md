# CIS 444/544 - Semester Project

This document outlines the semester-long project for CIS 444/544 Data Analytics. This is a living document and changes, updates and expansions will be published throughout the semester. See the [Changes](#changes) section for the current list of updates over time.

## Scope

The goal for this project is to build a *comprehensive data analytics system* for a fictional organization. This project will consist of multiple components and skills:

* Database modeling, reverse engineering and diagramming
* Building advanced SQL queries including use of analytic functions and in-database programmability
* Working with data across multiple database servers and database types
* Producing analytic dashboards for non-technical users so they can understand and visualize complex data
* Agile project management methodology and documentation

For your starting database, you have **three choices**:

* [**Employee Database**](https://dev.mysql.com/doc/employee/en/) - The Employees sample database provides a combination of a large base of data (approximately 160MB) spread over six separate tables and consisting of 4 million records in total. It is a simulation of employee records for a medium-sized enterprise.
* [**Sakila**](https://dev.mysql.com/doc/sakila/en/) - The Sakila database is a normalized schema modelling a DVD rental store, featuring things like films, actors, film-actor relationships, and a central inventory table that connects films, stores, and rentals.
* **Northwind** - An older but still useful sample database for a fictional organization "Northwind Traders". It encompasses key business areas such as customers, orders, order details, products, suppliers, shippers, employees, and territories.

> [!TIP]
> The web pages for some of these databases will describe the MySQL version. However, for this project you will be using a converted version for Microsoft SQL Server.

> [!IMPORTANT]
> The Northwind database is an old sample database from the 1990s. Dates and events in the database will appear to be quite old. 
>
> Additionally, the version of Northwind provided on the servers is *not the same as the original release* from Microsoft. Some data has been added to the database that is not documented or included in the original version. As part of your reverse engineering effort, you can identify data and tables associated with these features:
>
> * Geographic distribution: Products distributed across multiple warehouses globally
> * Customer feedback: Reviews with realistic rating distribution  
> * Supplier Performance: Quarterly evaluations with quality metrics
> * Supply chain tracking: IoT-style tracking data for recent shipments

## Project Deliverables

You will not be regularly submitting assignments for this project in class. Instead, you will be collecting and assembling your **project portfolio**, which you will submit during the final week of the course. Your project portfolio will consist of a large number of artifacts of your team's work throughout the semester. Artifacts you will include in your portfolio submission include, but aren't limited to:

* team documentation
* notes from sprint planning/retrospective meetings and standup meetings
* ERDs, data dictionaries and other database diagrams and documentation
* queries, code, etc. related to your project
* documentation on processes (e.g. ETL)
* your final presentation

Keep an eye on the *Deliverables* section for the current sprint - it outlines what you need to add to your portfolio each week.

> [!IMPORTANT]
> There will be a small number of individual, non-group, non-project assignments in this course. These assignments are *not* done as a group and *will* have individual due dates. Please keep an eye on D2L for due dates on individual assignments. The **only** course assignment that involves an end-of-semester large submission is the group project.

## Sprint Schedule

This section outlines the *high level tasks and topics* for the sprints in this course:

| Sprint | Weeks | Topic | Details (topics, assignments...) |
|-|-|-|-|
| &ndash; | 1-2 | Class intro, project overbiew | Lecture on big data terminology |
| 1 | 3-4 | Database Discovery & Project Foundation | Environment setup, database reverse engineering, ERD diagrams/data dictionaries |
| 2 | 5-6 | SQL Analytical Queries | Query List 1, data split ETL, MongoDB (non-linked) |
| 3 | 7-8 | Data Warehousing I | ETL for DW, data lake, validation, error handling, Query List 2 |
| 4 | 9-10 | Data Warehousing II | Star schema design, Fact/Dimension tables, Data marts |
| 5 | 11-12 | Reporting and BI | PowerBI dashboards, reports, KPIs/metrics |
| 6 | 13-14 | Integration and Testing | Finalize system, Documentation, Sprint/Project reporting |
| 7 | 15-16 | Final Presentation / Finals Week | Prepare and deliver final project presentation |

Details on each sprint will be **added below** as the class progresses, based on our progress and any decisions we make as a class or group.

### Sprint 1: Discovery

In Sprint 1, your primary task is to **get to know your databases**.

As part of this sprint, you will explore your existing database and design an **entity-relationship diagram** (ERD). You will also prepare a **data dictionary** (table schemas). 

You will:

* explore your database on the live cloud database server
* study the data to understand entities, their purposes and their meaning
* explore tools for reverse-engineering and understanding databases
* prepare complete documentation about your database and its structure

Additionally, you will formalize your group's Agile process. You will:

* agree on a time within your group for at least **four** stand-up meetings during the sprint
* conduct your first **sprint planning meeting** and schedule your **retrospective**
* decide on and implement an electronic project management strategy and platform (e.g. Trello, Jira)

#### Deliverables

Deliverables to include in your **final project portfolio** include:

* ERD diagrams
* Data dictionaries
* Written team "contract"/plan, outlining:
  * your team members and any identified strengths or roles you wish to assign (e.g. documentation lead, reporting lead)
  * your project management platform and strategy
  * your plan for scheduling standups and sprint planning/retrospective meetings

# Changes

This section details *changes* that have been made to this document. You should review this section *regularly* to identify any updates or additions to the project documentation and scope.

* 2025-09-01: First posting of project outline
