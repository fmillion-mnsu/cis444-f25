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
| 1 | 3-4 | Database Discovery & Project Foundation | Environment setup, database reverse engineering, ERD diagrams/data dictionaries, Query List 1 |
| 2 | 5-6 | MongoDB, Star Schemas for DW, Performance | Star and Snowflake schemas,  MongoDB (non-linked), ETL from SQL Server to MongoDB (Grad), Query List 2 (Mongo) |
| 3 | 7-8 | Data Warehousing I | TBD |
| 4 | 9-10 | Data Warehousing II | TBD |
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

Finally, you will begin writing your first **query list**. These queries are focused on improving your understanding of the actual data in the database.

- Query 1: Business Scale Analysis. "What is the scope and scale of this business?"

    Analyze table sizes and record counts to understand business volume

    Identify the primary operational focus areas

- Query 2: Stakeholder Identification. "Who are the key people/actors in this business ecosystem?"

    Profile the main human entities (customers, employees, actors, etc.)

    Analyze demographic distribution and key identifying characteristics based on available data.

- Query 3: Geographic Footprint. "Where does this business operate and serve customers?"

    Map the geographic distribution of business operations

    Identify primary markets and service areas

- Query 4: Operational Timeline. "What is the operational history and activity patterns of this business?"

    Determine the time span of business operations in your database

    Identify peak activity periods and business cycles

- Query 5: Value Analysis. "What generates value and revenue in this business?"

    Analyze monetary transactions and value indicators

    Identify high-value activities, products, or services

These queries should be implemented using standard SQL. At this time, don't use views, stored procedures or other programmability.

Document your queries as they will inform your understanding of the business domain for subsequent sprints. Keep your queries handy - you'll be improving and reworking them over time!

> [!HINT]
> The **Employee** database contains a lot of data, but fewer entities. You may find yourself struggling to apply all of these queries to Employee.
>
> If this is the case, you are free to use *any one* of the other two databases to write these queries. This will actually prepare you for the next phase - where we simulate a "company merger" and start building out our data warehouse.
>
> If you go this route, make sure you **document which database you used** in your queries (as a comment - hint: SQL Server comments are prefixed with two dashes - `-- This is a comment`).

#### Deliverables

Deliverables to include in your **final project portfolio** include:

* ERD diagrams
* Data dictionaries
* Written team "contract"/plan, outlining:
  * your team members and any identified strengths or roles you wish to assign (e.g. documentation lead, reporting lead)
  * your project management platform and strategy
  * your plan for scheduling standups and sprint planning/retrospective meetings
* Query List 1 queries

## Sprint 2: MongoDB, NoSQL and Star Schemas

In Sprint 2, you will learn about MongoDB and similar schemaless document databases, and you will form a process for copying your data from your SQL Server into MongoDB.

You will also begin designing - but not yet implementing - your star schemas. Start with choosing **two** of your query list business scenarios, and devise **star schemas** that would specifically support those business questions. 

> [!TIP]
> Remember: Star schemas are **de-normalized** by design - you should plan to reshape your existing data in such a way to maximize *performance* at the expense of storage size optimization. 

You will:

* ***Grad Students:*** Use Python (or another programming language) to write a simple **ETL tool** that will automatically migrate *all* data for your primary database (all tables and rows) from SQL Server to MongoDB.
* Convert your Query List 1 queries into MongoDB aggregation pipelines.
* Create appropriate indexes for your queries to ensure maximum performance
* Design and create ERDs for at least two star schemas based on your Query List 1 business questions. We will be implementing these schemas in *MongoDB* during Sprint 3.

#### Deliverables

Deliverables to include in your **final project portfolio** include:

* ERD diagrams for star schemas
* Query List 2 (MongoDB) aggregation queries
* Code for your ETL tool for migrating from SQL Server to MongoDB
* A description of, or the code for, indexes you create on your collections for performance optimization

## Sprint 3: Data Warehousing I

In Sprint 3, you will implement your data warehouse using star schemas and establish your ETL pipeline. This sprint marks the transition from exploration to implementation - you'll build the foundation of your analytics infrastructure.

Your primary database data is already in MongoDB from Sprint 2. You will now use MongoDB as your **data lake** - the source of truth for raw, unprocessed data. From there, you'll transform and load this data into SQL Server-based star schemas optimized for analytical queries.

You will:

* Design and implement at least **three star schemas** in Microsoft SQL Server
* Build a **Python ETL tool** that extracts data from MongoDB, transforms it according to your star schema design, and loads it into SQL Server
* **Rewrite relevant Query List queries** to take advantage of your new data warehouse structure
* ***Grad Students:*** Expand the MongoDB data lake to include data from the other two sample databases (preparing for a "company merger" scenario)
* ***Grad Students:*** Create a **merger integration plan** that documents how the three databases will be unified in Sprint 4

### Star Schema Design and Implementation

Based on your Query List queries and business scenarios, design at least three star schemas. Each schema should:

* Focus on a specific business question or analytical scenario
* Include at least one fact table and at least two dimension tables
* Follow star schema best practices (denormalization, appropriate grain, meaningful dimensions)
* Include a date/time dimension where appropriate!

> [!IMPORTANT]
> **Implementation requirements:**
> 
> * Create all tables in Microsoft SQL Server
> * Define appropriate primary keys, foreign keys, and indexes
> * Use appropriate data types that support analytical queries
> * Document your design decisions (why you chose certain dimensions, how you determined grain, etc.)

> [!TIP]
> **Example scenarios you might build star schemas for:**
> 
> * Sales analysis (if your database involves transactions)
> * Employee performance over time (if your database tracks employee data)
> * Inventory management (if your database includes products/stock)
> * Customer behavior analysis
> * Geographic distribution analysis

### ETL Pipeline Development

Build a Python-based ETL tool that:

* **Extracts** data from your MongoDB collections (your data lake)
* **Transforms** the data by:
    * Denormalizing related documents/tables into fact table records
    * Creating surrogate keys where needed
    * Calculating derived values (e.g., order totals, durations, aggregations)
    * Handling missing or null values appropriately
    * Formatting dates/times consistently
    * Populating dimension tables with distinct values
* **Loads** the transformed data into your SQL Server star schema tables

> [!IMPORTANT]
> **ETL Tool Requirements:**
> * Must be implemented in Python (or another language with instructor approval)
> * Should process all three of your star schemas
> * Should perform a full refresh (clear and reload) of the data warehouse
> * Should include basic error handling
> * Should log progress/results (e.g., number of records processed)

**Graduate Students:** Work with your group to ensure the ETL tool contains: 
* Transformation logic (perform a *transformation* - not just a straight copy of the data)
  * Consider how your star schemas are built - for example, you could use the ETL process to create your date/time table, combine or split people's names, normalize phone numbers to a standard format, etc.
* Comprehensive error handling and logging
* Documentation of your ETL architecture and design decisions

### Query List 3

Take your Query List 1 and Query List 2 queries and rewrite them to use your new data warehouse star schemas **where applicable**. 

You don't need to rewrite every query - focus on queries that:

* Use the entities/facts represented in your star schemas
* Would benefit from the denormalized structure
* Demonstrate the performance advantages of your DW design

For each rewritten query:

* Keep the original query for comparison
* Document what changed and why
* Note any performance improvements (if measurable)
* Explain how the star schema makes the query simpler or more efficient

### Graduate Students: Merger Preparation

In Sprint 4, we will be executing a "*merger*" - you will be importing the *other two databases* that you did not choose your primary database into your data lake, as if you and those other organizations have just merged. 

As you prepare for Sprint 4's company merger scenario, you need to expand your data lake and plan for integration.

#### Data Lake Expansion

Import data from the other two sample databases into MongoDB:

* If you started with Employees, import Sakila and Northwind
* If you started with Sakila, import Employees and Northwind  
* If you started with Northwind, import Employees and Sakila

You can reuse/extend your Sprint 2 ETL tool to accomplish this. Each database should be clearly organized in MongoDB (e.g., separate databases or clearly named collections). At this point, you don't need to do any transformations - just modify your existing ETL script to load the data for the other databases in its entirety.

#### Merger Integration Plan

Create a document that analyzes how the three databases will be unified. Your plan should include:

1. **Entity Mapping Analysis:**
   * Which entities exist across multiple databases? (e.g., all three have some concept of "people")
   * Which entities are unique to specific databases?
   * How do similar entities differ in structure across databases?

2. **Schema Comparison:**
   * Create comparison tables showing field-by-field differences for common entities
   * Identify fields that exist in some databases but not others
   * Note differences in data types, constraints, or formats

3. **Integration Strategy:**
   * How might you handle ID conflicts when merging? (e.g., customer IDs that overlap)
  
    > [!TIP]
    > Dimension tables need not necessarily be straight 1:1 mappings - a "Person" table might also include a "source ID" field...

   * What will your unified schema look like for merged entities?
   * How will you handle temporal differences? (databases cover different time periods)
   * What business rules will govern the merger? (e.g., "Northwind customers become 'legacy' customers")

4. **ETL Implications:**
   * What new transformations will be needed?
   * How will your star schemas need to change to accommodate merged data?
   * What challenges do you anticipate?

This plan will guide your Sprint 4 work and should be thorough enough that another team could implement your strategy.

You don't need to go overboard and there's no prescribed length requirement - feel free to be concise and treat this as both a deliverable and notes for your implementation during Sprint 4.

### Deliverables

Deliverables to include in your **final project portfolio** include:

* **Star schema ERDs** for at least 3 implemented schemas
* **SQL DDL scripts** for creating your data warehouse tables (unless you use ETL to create the tables for you!)
* **Python ETL tool** source code with documentation
* **Query List 3** - Rewritten queries from your Query Lists that utilize the data warehouse
* **Merger integration plan** document

### Tips for Success

* **Start with your simplest star schema** - get one working end-to-end before building the others
* **Test your ETL incrementally** - don't wait until everything is built to test data loading. You can use `TRUNCATE TABLE` to completely clear the data in a table (assuming no foreign key constraint would be violated).
* **Keep your MongoDB queries simple** - the goal is extraction; complex transformations should happen in Python
* **Use SQL Server's tools** - SSMS can help you verify data loaded correctly and test query performance
* **Document as you go** - it's much easier to document decisions when they're fresh
* **Collaborate on design** - have the whole team review star schemas before implementation begins
* Don't underestimate the merger analysis - discovering differences now will save time in Sprint 4!

# Changes

This section details *changes* that have been made to this document. You should review this section *regularly* to identify any updates or additions to the project documentation and scope.

* 2025-09-01: First posting of project outline
* 2025-09-22: 
    * Add full details for Sprint 2. 
    * Adjust sprint topics. (DW 1 and 2 are TBD based on progress during Sprint 2.)
* 2025-10-06: Add full details for Sprint 3 DW1.