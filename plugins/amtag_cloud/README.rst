amtag_cloud
=========

This plugin generates a tag cloud using _amcharts: https://www.amcharts.com/ framework.

Installation
------------

In order to use to use this plugin, you have to edit(*) or create(+) the following files::

      blog/
        ├── pelicanconf.py *
        ├── content
        ├── plugins +
        │     └── amtag_cloud.py +
        └── themes
              └── mytheme
                    ├── templates
                    │      ├── base.html *
                    │      └── amtag_cloud.html *
                    └── static
                          └── css
                               └── style.css *

In **pelicanconf.py** you have to activate the plugin::

    PLUGIN_PATHS = ["plugins"]
    PLUGINS = ["amtag_cloud"]

Into your **plugins** folder, you should add amtag_cloud.py (from this repository).

In your theme files, you should change **base.html** to apply formats (and sizes) defined in **style.css**, as specified in "Settings", below.

Settings
--------

================================================    =====================================================
Setting name (followed by default value)            What does it do?
================================================    =====================================================
``AMTAG_CLOUD=True``                                  Enable tag cloud  
``AMTAG_CLOUD_MAX_ITEMS = 100``                       Maximum number of tags in the cloud.
================================================    =====================================================

The default theme does not include a tag cloud, but it is pretty easy to add one. 

First you need to place **amtag_cloud.js** into your **static** directory. 

Then place following code into head of our **base.html**::
  <script src="https://www.amcharts.com/lib/4/core.js"></script>
  <script src="https://www.amcharts.com/lib/4/charts.js"></script>
  <script src="https://www.amcharts.com/lib/4/plugins/wordCloud.js"></script>
  <script src="https://www.amcharts.com/lib/4/themes/animated.js"></script>
  <script src="static/amtag_cloud.js" ></script>



The last - include code below into **base.html** and add **amtag_cloud.html** in your theme/templates directory::

        {% if AMTAG_CLOUD %}
          {% include 'amtag_cloud.html' %}
        {% endif %}


In the code above if used **animated** amcharts theme. But you could easy to use another one by modifiyng  *animated* word in base.html and amtag_cloud.html to another amcharts theme.