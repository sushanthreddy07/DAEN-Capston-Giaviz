 Real-Time Situational Awareness (RTSA)
This project aims to fuse disparate data sources to provide a unified, real-time view of situations, helping decision-makers respond faster and more effectively during crises. We're creating a system that turns overwhelming amounts of raw data into clear, actionable insights that can save time, resources, and lives.

🎯 Project Mission & Goals
Our goal is to build a platform that empowers emergency responders, city planners, and authorities by:

Integrating real-time and historical data from the Maryland, D.C., and Virginia (DMV) region. We're aiming for a data latency of under 10 minutes.

Utilizing machine learning and computer vision to automatically detect hazards, predict route blockages, and suggest alternate paths.

Visualizing all of this in an intuitive 3D environment, making complex information easy to understand and act upon during high-pressure situations.

Imagine a wildfire blocking a major highway. Our platform could instantly reroute fire engines, coordinate with utility crews to assess power grid damage, and suggest safe evacuation paths for citizens.

🔧 Project Architecture
Our plan is to execute this project in four key phases:

1. Data Collection & Integration

We will be gathering a wide range of data, from real-time feeds (traffic incidents, weather sensors, and flight tracking) to historical and static datasets (infrastructure maps, power outage records, and disaster archives).

2. Data Processing & Fusion

All collected data will be cleaned, normalized, and intelligently fused into a single, comprehensive model. This process ensures that spatial, temporal, and contextual information are unified.

3. Machine Learning & Computer Vision

We will leverage advanced algorithms to analyze incoming data. Our models will be trained to detect incidents from camera feeds, predict alternate emergency routes, and forecast the potential impact of an incident on critical infrastructure.

4. Interactive 3D Visualization

Using the GaiaViz platform, we will create a real-time, interactive 3D visualization. This will overlay all incidents, infrastructure, and predictive analytics in a single, easy-to-interpret view, enabling rapid decision-making.

📊 Key Data Sources
We will be working with both real-time and non-real-time datasets:

Real-time (<10 min latency): Maryland CHART traffic feeds, VDOT SmarterRoads data, weather APIs, and ADS-B flight tracking.

Non-real-time (historical or static): GIS infrastructure maps, power outage archives, and historical disaster incident data.

🚀 Current Status
We are currently in Phase 1: Dataset Discovery and Scoping. Our immediate next steps are to:

Finalize our data sources for the DMV region.

Set up data pipelines for ingestion and cleaning.

Begin building initial prototypes for data fusion and visualization.

Start experimenting with computer vision models to analyze live traffic feeds.

📚 References & Inspiration
Our work is inspired by leading research in smart mobility, disaster response, and operational planning. The following references have been instrumental in our project's development:

H. Xu et al., Smart Mobility in the Cloud: Enabling Real-Time Situational Awareness and Cyber-Physical Control Through a Digital Twin for Traffic, IEEE Access, 2022.

D. Correa and J. C. Falcocchio, A Data-Driven Case Study Following the Implementation of an Adaptive Traffic Control System in Midtown Manhattan, Journal of Transportation Engineering, 2022.

M. Bouabid and M. Farah, GAZADeepDav: A High Resolution Geotagged Satellite Imagery Dataset For Analyzing War-Induced Damage, IGARSS, 2024.

M. Chmielewski, Data Fusion Based on Ontology Model for Common Operational Picture Using OpenMap and Jena Semantic Framework, Military University of Technology, Warsaw, Poland.

📌 License
This project is licensed under the Creative Commons Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0) license, in alignment with our partner's intellectual property requirements.

Based on the roles assigned, here is an explanation of the team's structure and responsibilities:

Team Roles

Susanth Reddy Rachel - Scrum Master: Susanth is responsible for guiding the team in following Agile and Scrum principles. The Scrum Master facilitates meetings, removes obstacles, and helps the team stay on track to meet its goals.

Madhu Yamini Nainala - Product Owner: Madhu is the voice of the customer. The Product Owner is responsible for defining the product vision, managing the product backlog, and prioritizing features to ensure the team is building the right product.

Shri Ram Jawahar Vennela - Developer: As a developer, Shri Ram is part of the team that builds the product. This role involves designing, coding, testing, and maintaining the software.

Uday Sai Shankar Kola - Developer: Uday is also a developer, contributing to the creation of the product. This role is a key part of the development team and involves the technical work of building the project.

Chrissie Raj Benzam - Developer: Chrissie is another developer on the team, responsible for the technical implementation of the project.
