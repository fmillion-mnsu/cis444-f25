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

### Deliverables

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

## Sprint 4: Data Warehousing II - Data Marts, Company Merger and Reporting Prep

This sprint will focus on a **merger scenario** - where all of the databases we started with ultimately form a "merged" corporation.

This will present some unique and interesting challenges:

* How to map data elements between different source databases
* How to handle gaps (each database will have different dates of data)
* How to attempt to match common values (if any)
* Decision: do we integrate all the databases together for future OLTP, or do we allow the databases to continue to exist independently?

### Data Merge

If you didn't already complete it in Sprint 3, load the data from the other two databases (the two you didn't start with) into your MongoDB instance. You can either create a new database to hold the collections, or you can load everything into one database using a schema of your choosing (e.g. prefix all Sakila tables with `Sakila_`).

Update your ETL scripts that you wrote to move the first database to MongoDB and use the same scripts to load the new databases. At this stage, it is acceptable to have your ETL scripts simply delete all data in the target tables/collections and reload from scratch. We'll explore alternative strategies in Sprint 5.

### ETL Updates for Data Warehouse

If you haven't already, consider how you can *adapt your ETL processes for your data warehouse* - your star/snowflake schemas - to *incorporate data from the other database(s)* in your new data lake.

If none of your query list queries, star schemas, etc. support this, you should create a new scenario and schema. It's OK for you to change your analytics scenarios at this point - but part of this exercise will be *planning for your dashboard* - it's worth considering a scenario accordingly! (See below.)

Update your ETL tasks to *load data from multiple source databases* into the *same dimension and fact tables*. This will usually necessitate a custom field mapping and/or custom transforms for each source database - this is part of the ETL process! Then run your ETL and check the results using the same queries you already wrote for your fact tables.

### Views, Procedures, and Analytics

In this sprint, you'll also begin preparing for your analytics dashboard. To make this process straightforward, you should begin considering the *analytical queries you can run against your data warehouse* in order to produce results of interest. *Particularly,* you want your queries to have at least one variable - something that the user of the dashboard can change to adapt the visualization. An easy example is ability to select a month and year for a time-based visualization, but use your imagination!

Write at least **three queries** in the form of views or stored procedures. Two of those three queries should incorporate **at least one variable** that can be changed during analytics querying.

### Data Marts

Create at least two **department-specific data marts** in your database. This will, again, require an ETL process! You can move data *from the data warehouse* directly into your data *mart* tables.

For data marts, consider who the "owners" of those data marts are. For example, you could have the "finance" data mart as well as the "sales" data mart. The finance data mart might include only aggregate figures (e.g. sales per day) and/or only contain specific data relevant for financial analysis (e.g. including only the totals of transactions, not the individual order lines). Similarly, the sales data might not include as much financial data but might focus on categorical organization or "unit sales" data.

Write ETL processes to create these data mart tables. Include your ETL scripts in your deliverables.

### Data Validation

You can consider this a lower priority deliverable for this sprint, but if you make it through the earlier elements and need some more activity, you can start to consider a *data validation strategy*. This will be covered more in depth during Sprint 5.

In particular, you could:

* Design a tool that reads and verifies data - for example, ensures that the state field in all addresses is a valid state (accounting for variances in capitalization for example), or
* Ensure your data warehouse tables have constraints to enforce data safety, *and* incorporate handling in your ETL tools to deal with data that can't be inserted due to non-conformance

Start considering how you'll implement this during Sprint 5. If you are *way* ahead feel free to start working on this - we'll discuss this more near the end of Sprint 4.

### Graduate Students: ORM Exercises

For graduate students, you'll be working on ETL but you'll be focusing on using an **object-relational mapper** to do ETL, rather than bare SQL scripts and cursors. There will be a lecture on ORMs during the sprint during which we'll cover the specific additional requirement for graduate students for this section.

### Deliverables

This sprint contains a wider variety of different types of tasks. As usual, simply include scripts, screenshots, journals, etc. as appropriate to demonstrate your implementation of:

* Updated ETL to load all three databases from SQL Server to MongoDB
* Updated ETL scripts that bring in data from multiple sources (possibly doing different transforms per source) and loading data into your star/snowflake schemas
* Scripts for views/stored procedures in preparation for analytics
* ETL for data mart creation
* If you get to it: Plan for data validation - how will you validate each field (What are the requirements for each field to be considered valid)?
* Graduate students: ORM specific program code as discussed during the ORM lecture

## Sprint 5: Analytics Dashboards and Data Governance

In Sprint 5, you will begin to build your analytics dashboards and implement a comprehensive data governance system. This sprint bridges the technical data infrastructure you've built with the business intelligence that stakeholders need to make decisions.

You will transition from building data pipelines to creating the visual analytics layer while establishing governance practices that ensure data quality and trustworthiness.

### Overview

Sprint 5 has two primary focus areas:

1. **Data Governance Database (DGDB)** - A system for tracking ETL operations, validation rules, and data quality
2. **Analytics Dashboard** - At least one Power BI dashboard that visualizes your data warehouse insights

### Part 1: Data Governance Database (DGDB)

The Data Governance Database is a separate database (or schema within your existing database) that tracks your data operations and enforces data quality standards.

#### DGDB Purpose

Your DGDB should accomplish these goals:

* Track ETL run history (when jobs ran, how long they took, success/failure status)
* Store validation rules that your ETL processes enforce
* Log validation results (which records passed/failed which rules)
* Document your data merger logic and transformations
* Provide data for governance reporting and dashboards

#### DGDB Schema

While you're free to design your own schema, here's a suggested starting point:

```
ETL_Runs Table:

* Run_ID (PK)
* ETL_Job_Name (which ETL process ran)
* Start_DateTime
* Duration_Seconds
* Status (Success/Failure/Partial)
* Records_Processed
* Records_Rejected
* Notes/Error_Messages (e.g. TEXT field that can contain an entire log. Alternatively, omit this field and use another table to store many individual log entries tied to runs by Run_ID)

Validation_Rules Table:

* Rule_ID (PK)
* Rule_Name (machine-readable)
* Created_Date
* Rule_Description (plain English explanation)
* Rule_Category (e.g., 'Referential Integrity', 'Business Logic', 'Format Validation')
* Severity_Level (e.g., 'Critical', 'Warning', 'Info')
* Rule_Logic (SQL or Python logic that implements the rule) This one will take some thought - how can you represent a rule in an SQL table? You could do regular expression matching, simple type checks, or even a complex JSON-based definition format. Use your imagination!
* Is_Active (boolean - allows disabling rules without deleting them)

**Validation_Results Table:**
* Result_ID (PK)
* Run_ID (FK to ETL_Runs)
* Rule_ID (FK to Validation_Rules)
* Validation_DateTime
* Records_Checked
* Records_Passed
* Records_Failed

**Data_Lineage Table** (optional but recommended):
* Lineage_ID (PK)
* Source_System (e.g., 'MongoDB - Sakila', 'MongoDB - Northwind')
* Source_Table
* Target_System (e.g., 'SQL Server DW')
* Target_Table
* Transformation_Description
* Last_Updated
```

Feel free to add, remove, or modify tables as needed for your implementation!

#### Validation Rules Implementation

Your validation rules should operate at multiple tiers:

##### Tier 1: Required Validations (Everyone)

Implement at least **3-5 validation rules** from these categories:

* **Referential Integrity:** Beyond basic FK constraints - verify that relationships make sense across your merged data
* **Non-Null Critical Fields:** Ensure essential business fields are populated
* **Positive Values:** Prices, quantities, and other measures that must be positive
* **Data Type/Format Consistency:** Dates formatted correctly, phone numbers standardized, etc.
* **Value Range Reasonableness:** Values within plausible ranges (even if historical)

##### Tier 2: Encouraged Validations

If time permits, add rules like:

* **Cross-Field Logic:** End dates after start dates, employee termination after hire date, etc.
* **Statistical Outlier Detection:** Flag unusually high/low values for manual review
* **Business Rule Enforcement:** Domain-specific rules from your business scenario

##### Tier 3: Advanced rules

This section can be focused on by graduate students - implement at least **2 additional advanced rules:**

* **Cross-Database Consistency:** Verify that merged data from different sources maintains logical consistency
* **Historical Data Reasonableness:** Account for different time periods across datasets
* **Complex Multi-Condition Rules:** Business rules with multiple dependencies

#### Merger Logic Documentation

One of your most important validation tasks is documenting and validating your data merger strategy. Create validation rules that verify your merger transformations are working correctly.

**Examples of merger validation rules:**

* "All Sakila customer IDs have 'SAK-' prefix in merged customer dimension"
* "Products from Northwind have source_system = 'Northwind' in product dimension"
* "Employee records span expected date ranges: Employees DB (1985-2002), Northwind (1996-1998)"
* "No ID collisions exist across merged data sources"

**Documentation Requirements:**

1. **Plain English Rules Document** - Create a document (or section in your portfolio) that explains:
   * How you handled ID conflicts during the merger
   * What prefixes, suffixes, or key transformations you applied
   * How you mapped similar entities across databases (e.g., all three databases have "people")
   * What assumptions you made about data compatibility
   * How you handled temporal differences (different date ranges)

2. **Rules in DGDB** - Store these merger rules in your Validation_Rules table so your ETL can:
   * Parse and execute them programmatically
   * Log the results to Validation_Results
   * Alert when merger logic fails

#### ETL Updates

Retrofit your existing ETL code (from Sprints 3 and 4) to:

1. **Log ETL Runs:** Every time your ETL runs, insert a record into ETL_Runs
2. **Execute Validation Rules:** Read rules from Validation_Rules table and execute them
3. **Log Validation Results:** Write outcomes to Validation_Results table
4. **Handle Validation Failures:** You have choices on how to handle failures:
   * **Strict Mode:** Reject records that fail critical validations
   * **Logging Mode:** Load all records but flag failures in DGDB
   * **Hybrid:** Reject on critical failures, log on warnings
   
   Document your choice and implement consistently!

5. **Error Handling:** Capture and log any ETL errors or exceptions

### Part 2: Analytics Dashboard Development

Create at least **one comprehensive dashboard** during Sprint 5, with the expectation that you'll complete a second dashboard in Sprint 6.

#### Dashboard Requirements: Executive/Global Dashboard (Priority for Sprint 5)

This dashboard should provide a high-level view of your entire "merged company" using data from your data warehouse (star/snowflake schemas).

**Required Elements:**

* **Minimum 4 meaningful visualizations** - each should answer a specific business question
* **At least 1 interactive element** - filters, slicers, drill-downs, date range selectors, etc.
* **KPI cards or metrics** - high-level numbers that executives care about
* **ETL/Data Quality Visualization** - incorporate data from your DGDB to show:
  * Recent ETL run status
  * Data quality trends
  * Validation pass rates
  * Or similar governance metrics

**Visualization Quality:**

Focus on creating visualizations that tell a story and provide actionable insights. Don't create meaningless charts just to meet a count requirement. Each visualization should:

* Answer a clear business question
* Use appropriate chart types for the data
* Include proper labels, titles, and formatting
* Be easy to interpret at a glance

##### Dashboard 2: Department-Specific Dashboard (Sprint 5 or 6)

This dashboard should dive deep into one business area using data from one of your data marts.

**Required Elements:**

* **Minimum 4 meaningful visualizations**
* **At least 1 interactive element**
* **Focus on departmental KPIs** - metrics relevant to that specific business unit
* **Comparison/Trend Analysis** - show changes over time or comparisons between categories

**Examples of department dashboards:**
* Sales Performance (products sold, revenue trends, top customers)
* HR Analytics (headcount, retention, hiring trends)
* Financial Performance (revenue, expenses, profitability)
* Operations (inventory, fulfillment times, efficiency metrics)

#### Technical Requirements

* **Tool:** Power BI Desktop (free version) is recommended, but you may use alternatives (Tableau, Looker, etc.) if you can meet all deliverables
* **Data Connection:** Connect to your SQL Server data warehouse/data marts (not the data lake in MongoDB)
* **Documentation:** For each dashboard, document:
  * What business questions it answers
  * Who the intended audience is
  * What data sources it uses
  * Any calculations or transformations you performed

#### Graduate Students: Advanced Analytics

Graduate students should incorporate **advanced analytics features** into their dashboards:

**DAX**

Create at least **2-3 calculated measures using DAX** (Data Analysis Expressions). These should go beyond simple sums or counts.

**Examples of DAX measures to implement:**

* **Year-over-Year Growth:**
  ```
  YoY Growth % = 
  DIVIDE(
      [Current Year Sales] - [Previous Year Sales],
      [Previous Year Sales]
  )
  ```

* **Running Total:**
  ```
  Running Total Sales = 
  CALCULATE(
      [Total Sales],
      FILTER(
          ALLSELECTED(Date[Date]),
          Date[Date] <= MAX(Date[Date])
      )
  )
  ```

* **Moving Average:**
  ```
  30-Day Moving Avg = 
  CALCULATE(
      AVERAGE(Sales[Amount]),
      DATESINPERIOD(Date[Date], LASTDATE(Date[Date]), -30, DAY)
  )
  ```

* **Percentage of Total:**
  ```
  % of Total Revenue = 
  DIVIDE(
      [Total Sales],
      CALCULATE([Total Sales], ALL(Product[Category]))
  )
  ```

##### Encouraged: Advanced Visualizations

You're also encouraged to implement (focus can be on graduate students):

* **Forecasting:** Use Power BI's built-in forecasting on time-series data
* **What-If Analysis:** Create parameters that allow users to model scenarios
* **Advanced Filtering:** Complex filter logic using DAX

### Deliverables

Add the following to your **final project portfolio**:

1. **DGDB Schema:**
   * SQL DDL scripts for creating your DGDB tables
   * Documentation of your schema design choices

2. **Validation Rules Documentation:**
   * Plain English document explaining your validation rules
   * Special focus on merger logic documentation
   * Explanation of how you handle validation failures

3. **Updated ETL Code:**
   * Modified ETL scripts that integrate with DGDB
   * Code should log runs, execute validations, and record results
   * Include comments explaining governance integration
   * *Don't* remove your old code - keep that stored as a historical artifact. Store your updated code under a new name or directory.

4. **At Least One Dashboard:**
   * Power BI .pbix file (or equivalent for other tools)
   * Screenshots of your dashboard
   * Documentation explaining:
     * Business questions it answers
     * Intended audience
     * Data sources used
     * Key insights or findings

5. **Sprint Documentation:**
   * Sprint planning notes
   * Standup meeting notes (at least 4 during this sprint)
   * Sprint retrospective notes

### Looking Ahead: Final Presentation

As you build your dashboards, start thinking about your final presentation. Your dashboards will likely be a centerpiece of that presentation - they demonstrate the business value of all the technical work you've done.

Consider:
* What story do your dashboards tell about the business?
* What interesting insights have you discovered?
* How would a real company use what you've built?

We'll formalize presentation requirements in Sprint 6, but keeping this in mind now will make that sprint smoother!

# Changes

This section details *changes* that have been made to this document. You should review this section *regularly* to identify any updates or additions to the project documentation and scope.

* 2025-09-01: First posting of project outline
* 2025-09-22: 
    * Add full details for Sprint 2. 
    * Adjust sprint topics. (DW 1 and 2 are TBD based on progress during Sprint 2.)
* 2025-10-06: Add full details for Sprint 3 DW1.
* 2025-10-20: Add full details for Sprint 4 DW2.
* 2025-11-04: Add full details for Sprint 5 DG/PBI.