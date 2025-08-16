# CIS 444 / 544 – Data Analytics - Syllabus

Minnesota State University, Mankato. College of Science, Engineering, & Technology.

*Fall 2025, All Sections.*

This course is offered on an In-Person Only basis. In-person attendance is required for each course session.

This is a 4-credit course for Computer Information Science majors or graduate students.

> **Catalog Description:**
> 
> The course explores big data in structured and unstructured data sources. Emphasis is placed on big data strategies, techniques and evaluation methods. Various data analytics are covered. Students experiment with big data through big data analytics, data mining, and data warehousing tools.

## Class Time and Place

- **Semester/Block**: Fall 2025 (8/26/2023 through 12/9/2023), 29 class sessions
- **Days and Time**: Tuesdays and Thursdays, 10:00 AM - 11:50 AM ([iCalendar File](https://github.com/fmillion-mnsu/cs470-s25/raw/master/cs470.ics))
- **Location:** WH 283 ([Building Map](https://www.mnsu.edu/globalassets/maps/university/buildings/2021/wh_02_secondfloor_2021.pdf))

## Instructor

- **Name**: Flint Million (he/him)
- **Email**: [flint.million.2@mnsu.edu](mailto:flint.million.2@mnsu.edu)
- **Office / Student Support Hours**: By Appointment - please E-mail to request

### Email Policy

It's important to me that I be available to help you succeed in this course. If you need to contact me, please send me an E-mail. I try to answer all emails within 24 hours, including weekends - even if I need more time to respond, I will acknowledge receipt of your message. **If I have not responded to your E-mail message after 24 hours, please resend the message** in case it got lost or buried. *Do not feel you need to wait longer than 24 hours* to resend your message - I would rather see your message more than once than miss your questions!

### Scheduling a Meeting

If you would like to meet with me directly, you can schedule time with me to meet in my office. Please contact me via E-mail, or see me before or after class, and I will accommodate your time schedule to the best of my ability.

## Course Description

This course will introduce you to techniques in advanced data analysis and analytics. You will learn:

* role of database architects
* database modeling with reverse engineering
* data models: organization master data model (OMDM), star schemas
* advanced SQL programming techniques 
* OLTP vs. OLAP
* modern programming systems for databases (examples: Python in SQL Server, PostgreSQL extensions)
* non-relational database engines and how they fit into a data analytics architecture
* big data management strategies: data lakes, data marts and data warehouses
* data governance strategies and techniques

> **Graduate Students**
>
> Graduate students will take on a leadership role in their groups and will focus on implementing advanced systems, such as:
>
> * using external code to access and process database data
> * building and deploying visualization systems, dashboards, and other tools for stakeholders and other non-technical data consumers
> * exploring new and emerging database and big data analytics technologies

In this course, you will be working on a large semester-long data engineering project in which you will design a complete full stack data analytics architecture, along with reporting systems for stakeholders and non-technical audiences. You will implement each stage of the project in **sprints** following the Agile software development methodology. Details on the project are contained in the [project description](PROJECT.md) document.

## Textbook

You do not need to purchase a textbook for this course. However, we will use various Internet resources regularly throughout the course.

## Prerequisites

CIS 440, equivalent transfer course, or instructor permission.

## Requirements

You will be participating in in-class activities that require a laptop to be brought to class. If you do not have access to a personal laptop, you can borrow one from the University Library.

D2L will be used to provide you with course announcements, homework assignments, course materials and quizzes. Official course announcements will also be sent to you via your university E-mail address. You are responsible for regularly checking D2L and your university E-mail for communications.

## Group Project

This course will involve a major group project that you will work on in small groups of 3-4 students throughout the duration of the semester. 

# Course Schedule (Weeks 3-15)

| Week # | Overall Topic | Specific Steps |
|--------|---------------|----------------|
| **Weeks 3-4**<br/>(Sprint 1) | **Project Management Setup, Data Modeling Fundamentals, and Initial Database Exploration** | **Lectures:**<br/>- **Agile Methodology and Scrum:** Introduce concepts like sprints, product backlog, daily scrum, sprint planning, roles (ScrumMaster, Product Owner, Team).<br/>- **Data Modeling:** Cover Conceptual, Logical, and Physical Data Models. Focus on **Entity-Relationship Diagramming (ERD)** components (entities, attributes, relationships: 1-M, 1-1, M-M) and their **conversion rules to a relational database** model.<br/>- **Introduction to System Catalogs:** Explain their purpose and how to query them in Oracle and MSSQL for metadata.<br/><br/>**Group Work/Project Steps:**<br/>- Students will formalize their class groups (formed in Week 1).<br/>- **Set up Team Trello Boards** for project management and define initial product backlogs for the semester-long project.<br/>- Begin exploring assigned databases in Docker environments.<br/>- Perform **reverse engineering to produce data models** (e.g., using Microsoft Visio) for assigned databases and compare them with intended models.<br/>- Utilize **System Catalog commands** to list schema, table names, and record counts for databases in Oracle and MSSQL.<br/>- Introduce the **Data Governance Database (DGDB)** as a central metadata repository.<br/><br/>**Sprint 1 Deliverables (Enhanced):** Submit initial Trello setup, sprint planning document, initial scrum reports, project reports (introduction, sprints, scrum report, appendix with initial data exploration and model comparisons), and presentation artifacts. Focus on documenting initial database structures. |
| **Weeks 5-6**<br/>(Sprint 2) | **Advanced SQL for Data Exploration & Basic Data Analysis with Pivot Tables** | **Lectures:**<br/>- **Advanced SQL Functions:** Dive into analytical capabilities with `CASE` expressions, `DECODE` function, `GROUP BY` with `ROLLUP` and `CUBE` operators, and ranking functions like `RANK` and `DENSE_RANK`, `NTILE`.<br/>- **Pivot Table Fundamentals:** Explain the anatomy of a pivot table (values, row, column, report filter areas), and guide students through creating basic pivot tables in Excel.<br/>- **Introduction to Data Warehousing Concepts:** Lay the groundwork by defining key characteristics like subject-oriented, integrated, time-variant, and non-volatile data.<br/><br/>**Group Work/Project Steps:**<br/>- Implement **Query List 1 (System Catalog Queries)** using advanced SQL commands against Oracle System Catalog (OSC), MSSQL System Catalog (MSC), and DGDB.<br/>- Analyze the results from Query List 1 using **Pivot Tables** in Excel, producing visual reports and charts.<br/><br/>**Sprint 2 Deliverables (Enhanced):** Submit updated product and sprint backlogs, detailed scrum reports, comprehensive project reports (including a comparative analysis of SQL vs. Pivot table results for Query List 1), and presentation artifacts. Students should now have a solid understanding of extracting and summarizing metadata. |
| **Weeks 7-8**<br/>(Sprint 3) | **Database Programming & Interactive Pivot Dashboards** | **Lectures:**<br/>- **PL/SQL and T-SQL Programming:** Cover control structures (`IF-THEN-ELSE`, loops), cursors for row-by-row processing, and the development of **Stored Procedures** and **User Defined Functions (UDFs)**.<br/>- **Database Objects:** Detail the creation and usage of **Views** (including grouped and joined views) and **Materialized Views** (for performance), and **Triggers** for automating database actions, auditing, and enforcing integrity constraints.<br/>- **Advanced Pivot Table Features:** Explore grouping numeric and date fields, performing calculations, and designing interactive dashboards (e.g., using slicers).<br/><br/>**Group Work/Project Steps:**<br/>- Re-implement **Query List 1** (System Catalog Queries) using **database programming (Stored Procedures, UDFs, Views)** against OSC, MSC, and DGDB.<br/>- Design and implement a **Pivot User Interface (PUI)** using Excel, creating linked sheets to present interactive data analysis.<br/><br/>**Sprint 3 Deliverables (Enhanced):** Submit updated backlogs, scrum reports, project reports (comparing SQL and DB Programming implementations, and PUI design documentation), and presentation artifacts. Students should demonstrate ability to automate data extraction and create more dynamic reports. |
| **Weeks 9-10**<br/>(Sprint 4) | **Data Warehouse Design & OLAP Fundamentals** | **Lectures:**<br/>- **Data Warehousing Design:** Deep dive into **Dimensionality Modeling**, differentiating it from ER modeling. Focus on designing **Fact Tables and Dimension Tables** to create **Star Schemas**.<br/>- **Online Analytical Processing (OLAP):** Introduce key OLAP analytical operations like **Roll-up, Drill-down, Slice, Dice, and Pivot**. Discuss the architecture and categories of OLAP tools (MOLAP, ROLAP).<br/>- **Fuzzy Active Databases:** Introduce the concept of **Fuzzy Logic** and its application in active databases for performance evaluation, linking to Query List 2.<br/><br/>**Group Work/Project Steps:**<br/>- Implement **Data Marts** (as views) for **Query List 1** (System Catalog), **Query List 2** (Fuzzy Queries on FAOES database), and **Query List 3** (MLS2 Player, Team, and Referee Performance analysis).<br/>- Connect Excel Pivot tables to these newly created data mart views to perform ad-hoc analysis and reporting.<br/><br/>**Sprint 4 Deliverables (Enhanced):** Submit updated backlogs, scrum reports, project reports (including detailed star schema designs, data mart implementations, and analytical reports from Pivot tables), and presentation artifacts. Students will demonstrate ability to design and query data warehouses. |
| **Weeks 11-12**<br/>(Sprint 5) | **Modern Analytical Tools: Power BI & Python for Big Data** | **Lectures:**<br/>- **Power BI (PBI):** Provide an overview of Power BI's capabilities, including connecting to various data sources, designing user interfaces, creating interactive dashboards, and visualizing complex data.<br/>- **Python for Data Access:** Cover fundamental Python libraries for connecting to and retrieving data from both relational databases (using SQL) and **NoSQL databases (specifically MongoDB)**.<br/>- **MongoDB Concepts:** Introduce MongoDB as a document-oriented NoSQL database, explaining **JSON/BSON document structure**, and demonstrating basic queries (`$match`, `$group`, `$sort`, `$limit`) and aggregation pipelines.<br/><br/>**Group Work/Project Steps:**<br/>- Implement **Query Lists (1, 2, and 3)** using **Power BI** to create advanced visualizations and interactive reports. Compare the results and functionalities with previous Pivot table implementations.<br/>- Implement **Query List 1** using **Python** scripts to interact with databases and retrieve data. Compare Python implementations with earlier SQL implementations.<br/><br/>**Sprint 5 Deliverables (Enhanced):** Submit updated backlogs, scrum reports, project reports (showcasing Power BI dashboards and Python scripts, with comparative analysis), and presentation artifacts. Students will be proficient in using modern BI and scripting tools. |
| **Weeks 13-14**<br/>(Sprint 6) | **Distributed Database Systems & Query Optimization** | **Lectures:**<br/>- **Distributed Databases (DDBS):** Cover core concepts such as **data fragmentation** (horizontal, vertical), **data replication**, and various types of **transparency** (location, fragmentation, replication). Discuss the advantages of distributed systems like local autonomy, reliability, and availability.<br/>- **Distributed Concurrency Control:** Explore the complexities of **distributed deadlocks** and mechanisms like **Two-Phase Commit (2PC)** and **Three-Phase Commit (3PC)** for ensuring transaction atomicity in distributed environments.<br/>- **Distributed Query Processing (DQP):** Explain strategies for optimizing queries across multiple sites, including understanding communication cost models and techniques like **semi-joins**. Introduce the concept of **Linked Services** for cross-DBMS queries.<br/><br/>**Group Work/Project Steps:**<br/>- Develop a **distributed database data model** based on a given strategy, considering regional data distribution and replication scenarios.<br/>- Re-implement selected **Query Lists (from Sprints 2, 4, and 5)** using **Distributed Query Processing (DQP)** by leveraging **Linked Services** from a central MSSQL server to query across various DBMS (Oracle, MSSQL, MongoDB).<br/><br/>**Sprint 6 Deliverables (Enhanced):** Submit updated backlogs, scrum reports, final project reports (documenting DDBS strategy, DQP implementations with screenshots, and comparative analysis with previous sprint results), and presentation artifacts. This will be the culmination of their project work on distributed systems. |
| **Week 15** | **Project Integration & Final Preparations** | **Specific Steps:**<br/>- This week is dedicated to **consolidating all work** from the previous sprints into a cohesive final project submission.<br/>- Students will focus on **reviewing their solutions, ensuring correctness and completeness** across all implemented query lists and database technologies.<br/>- Teams should use this time to **prepare thoroughly for their final project presentations**, refining their demo, narrative, and report.<br/>- **Finalize and submit the comprehensive Final Report**, which will integrate all aspects of the project, including methodologies, implementations, analysis, and conclusions. |

## Grading

This course is available on a for-credit, Grade Only basis. You will receive a letter grade in this course. Your final grade will be calculated according to the following rubric on the next page.

Your final grade for this course will be based on the following assessments and weights:

Item | Percent
---- | --------
Attendance | 5%
Individual Activities | 10%
Group Activity | 85%

**There will be no quizzes or final exam for this course.** The work you do in your individual and group assignments will be ongoing throughout the semester. Your final grade will be calculated based on the above categories.

This course will use shaded grading. The following is the minimum score for each grade:

Percentage of Points | Grade
-------------------- | -----
97% | A+
93% | A
90% | A-
87% | B+
84% | B
80% | B-
77% | C+
74% | C
70% | C-
67% | D+
64% | D
60% | D-
0% | F

### Deadlines

Assignment due dates in this course are firm. Unless you have extenuating circumstances that you discuss with me *as early as possible*, assignments submitted late will lose significant points, up to an including a full loss of points for the assignment.

Unless otherwise stated, assignments will be due on D2L (or via an appropriate alternative submission mechanism) at **11:59 PM** on the given due date.

In general, I will use the following penalties for late **individual assignments**. Exceptions or modifications to these will be noted as appropriate.

Submitted | Maximum score
--------- | -------------
On Time | 100%
1 day late | 85%
2 days late | 75%
3 days late | 65%
4 days or more late | No credit

Late submission days *include weekends*. (If an assignment is due on Friday at 11:59 PM, submitting on Monday counts as 3 days late!)

**Submitting group assignments late requires special permission from me. Since your main group project is due at the end of the course, I cannot accept late submissions on the final group project submission unless you have discussed your group's extenuating circumstances with me ahead of time.** Note that the above late days policy applies for any shorter group check-in assignments - more on this will be discussed in class.

### Attendance Grading

Because attendance is very important in small group project work, we will be taking attendance in this course. Each time you come to class, you will scan your MavCARD to present your attendance. More details on this will be given in class.

Attendance grading will comprise 5% of your final course grade. However, if attendance becomes a significant concern, your overall grade *may be lowered* due to significantly poor attendance, depending on the circumstances. *In general*, three or more full absences without notifying me of the situation may have a more significant effect on your grade. However, I consider attendance on a case-by-case basis - please reach out to me if you have concerns about your ability to attend the class at any point.

If you need to miss a class, you should contact me *as early as possible* to explain your situation. I will make reasonable accommodations for important activities that require you to be absent from class; if your absence is significant I may offer you some make-up work and/or the option to join the class via Zoom as appropriate. **Notifying me of an absence after the fact will NOT result in an excused absence unless the circumstances are particularly extreme and warrant such an accommodation.** Such exceptions will only be made on a case-by-case basis.

If I have given you an excused absence, you will receive attendance points for that day despite being absent.

### Grade Explanations and Appeals

You have the right to ask me for an explanation of any grade you receive, both on assignments as well as your final grade.

Grade appeals are reviewed in instances where students perceive that a final course grade is unfair, arbitrary, or capricious. Students must begin the procedures of this policy within two weeks of university notification of a final course grade. Students needing assistance at any step in appealing a grade may contact the Academic Affairs Coordinator of the Student Senate (280 Centennial Student Union; phone 389-2611). Students should retain copies of all materials associated with this process for their records. Students should also have records of their coursework from the class as part of the appeal process. The full policy is available at <http://www.mnsu.edu/policies/approved/gradeappeals.pdf>.

## Diversity Statement

The diversity of the participants in this course is a valuable source of ideas, problem solving strategies, and computational creativity. Our classroom is a place where you will be treated with respect, and we welcome individuals of all ages, backgrounds, beliefs, ethnicities, genders, gender identities, gender expressions, national origins, religious affiliations, sexual orientations, ability, and other visible and nonvisible differences. All members of this class are expected to contribute to a respectful, welcoming and inclusive environment for every other member of the class. If you are experiencing disrespect or any other inappropriate conduct from any classmate, please talk to me directly. Unless university policy requires otherwise I will keep such conversations confidential.

### Name and Pronouns

I will gladly honor your request to address you by an alternate name or gender pronoun. Please advise me of this preference early in the term so that I may make appropriate changes to my records. I also expect other students to respect and honor these requests when interacting in the course. If you are experiencing any disrespect from classmates please come talk to me.

## University Policies

Please review the following policies which will govern your activities in this course.

### Academic Honesty

As members of the University community, students assume the responsibility to fulfill their academic obligations in a fair and honest manner. This responsibility includes avoiding inappropriate activities such as plagiarism, cheating, or collusion. Students found responsible for one or more of these activities may face both academic sanctions (such as lowering a grade, failing of a course, etc.) and disciplinary sanctions (such as probation, suspension, or expulsion).

In this course, I encourage you to ask your peers and utilize available online resources for assistance with projects and homework. However, such assistance must not include sharing or copying of code or solutions. All work you submit for your projects or assignments must be written by you or your group members alone. Here are some examples:

* Helping your classmate or another group understand why their syntax is causing a compilation error is OK; fixing it for them or providing a copy of your code to your classmate is not.
* Asking a classmate, group or online forum a question about why your code is not doing what you expect it to, and receiving answers guiding you to a solution that you implement yourself, is OK; asking someone to fix the code *for* you or simply provide you with working code that you will use as-is is not.
* Studying code online to learn how something is done and then implementing that solution in your own way is OK (as long as you understand and can explain your code); copying and pasting large amounts of code verbatim or with only very minimal changes is not.
* **My policy on use of artifical intelligence is covered in a separate section below.**

This course includes a group project. For the group project, specific requirements for submission of completed work will be outlined for that specific project. Each group will submit both a final group project deliverable *in addition to* individual submissions. For all work outside the group project, unless otherwise noted, you should assume *all* homework is to be completed and submitted **individually**.

The full policy, including definitions of plagiarism, cheating, and collusion, is available at <https://www.mnsu.edu/policies/approved/academichonesty.pdf>.

### Artificial Intelligence Policy

I treat code or other text generated with artificial intelligence the same way I treat materials obtained from a human-generated source (website post, book, classmate&hellip;). In other words, you *may* ask an AI system for assistance with your code and you *may* study code generated by the AI for ideas; however, you ***may not*** copy code provided by an AI engine verbatim or with only very minimal modification and include it as your own work. You *can* use AI as a tool to help you learn and as a reference, but you *cannot* (and should not!) use AI as a tool to "do the work for you".

As with any code you submit, you must **fully understand and be able to defend your code**. In any case, you may *not* share artifacts you generate with AI with any other classmates (with the obvious exception of sharing with your group members for group project work).

I exercise common sense in enforcing these policies. For example, if you discover that there is one single well-established strategy for accomplishing a given generic task and a template implementing that method is provided, and coding an alternative strategy would be excessively awkward or would create other secondary issues (e.g. insecure code, slower performance, etc.), then using such a template is not considered "copying and pasting large amounts of code verbatim".

> To illustrate this, consider that many IDEs provide templates for various project types and also often offer "wizards" that generate parts of the code for you based on parameters you specify, with the generated code following established coding practices. 
> 
> Use of such tools is *not* violation of this policy, since they are generic in nature and you are still required to write the code to make the application perform your specific tasks.
>
> However, asking an AI engine to write code for your *specific, unique* scenario, and then copying that code as-is, is a violation of this policy.

If you have further questions on this policy, or want to ask about a specific scenario, please feel free to ask me.

### Students with Disabilities

Minnesota State Mankato provides students with disabilities reasonable accommodation to participate in educational programs, activities or services, and I strive to make this course accessible and engaging for all learners, including students with disabilities. If you have a disability requiring accommodation to participate in class activities or meet course requirements, you should first register with the Office of Accessibility Resources (if you have not already) by following the process described at <https://mankato.mnsu.edu/university-life/campus-services/accessibility-resources/getting-started/> to establish an accommodation plan. Accessibility Resources will inform me about your needs in the course based on their records.

After this step, you can also choose to reach out to me and I will be happy to work with you directly to ensure all of your accommodations are provided to you and that you can participate fully in the course. Feel free to come to me or e-mail me any time if you are finding the course inaccessible in any way. I am happy to work directly with you to make any reasonable accommodation I can to ensure your success in this course. I will keep any information you share with me about your disability strictly confidential and will not disclose or discuss your disability with anyone else without your consent.

### Electronic Recording of Lectures and Materials

University policy states that students are not permitted to make unauthorized electronic recordings of lectures using personally owned recording devices (e.g., smartphone, iPad, computer, digital recorder) unless prior permission from the instructor is obtained, and there are no objections from other students.

Additionally, students are not permitted to make electronic copies of proprietary course materials (e.g., PowerPoints, formulas, lecture notes) without consent from the instructor. This does not apply to publicly available materials that are used in class.

If you need to record lectures or need course materials for an accessibility reason, please notify the Office of Accessibility Resources, and then discuss the matter with me as early as possible.

In any case where recording is permitted (even for accessibility purposes), recorded lectures or copied material must be destroyed at the end of the course or semester. Unauthorized downloading, file sharing, or distribution of any part of a recorded lecture or course materials, or using information from such recordings for purposes other than the student’s own learning, may be deemed a violation of Minnesota State University, Mankato’s “Statement of Student Responsibilities,” subject to disciplinary action.

The full policy is available at <http://www.mnsu.edu/atoz/policies/recordingoflecturesandmaterials2015.pdf>.

> The materials in this GitHub repository are licensed under CC-BY-SA and are publicly accessible on GitHub, and as such this policy does not apply to the materials in this repository. You may access, share and use these materials however you like provided you abide by the terms of the [CC-BY-SA 4.0 License](https://creativecommons.org/licenses/by-sa/4.0/deed.en).

### Missed Classes

Students represent the university through participation in university sponsored or sanctioned activities, such as the arts, theater, music, dance, forensics, and intercollegiate athletics. If an activity schedule conflicts with academic obligations, students will follow a standard protocol to provide their faculty members with prior, written notification of their absences from classes. Faculty members will determine, in consultation with students, how missed classes and assignments will be made-up in a manner that fulfills academic obligations and accommodates participatory obligations. Except for absences resulting from sponsored or sanctioned activities, student participants have the same responsibility with regard to class attendance and assignments as do all other students.

The full policy is available at <http://www.mnsu.edu/atoz/policies/missedclassesandmakeupwork.pdf>.

If you need to miss class for an important non-school-related reason (e.g., a medical appointment), please let me know ahead of time, as early as possible. I understand that sometimes extenuating circumstances may arise suddenly without warning. In this case, please contact me by E-mail as soon as you possibly can to let me know you will be unable to attend class and/or meet a deadline. Within reason we will work together to come up with a solution. The more openly we communicate, the easier it is for me to accommodate your situation!

If you test positive for COVID-19 but are *not symptomatic*, please come to class and wear a mask to protect others. If you *are* symptomatic, please let me know via E-mail as soon as possible and we can arrange for you to attend the course via Zoom temporarily.

### Veterans Information

As a particular acknowledgment of an individual's service to our country, faculty members are committed to providing resources to veterans/military students, which will assist in smooth navigation of the university environment and a successful educational experience. Resources for veterans are available at <http://www.mnsu.edu/veterans/resources>. *Student veterans and current military members with special circumstances or who are activated are encouraged to notify the instructor.*
