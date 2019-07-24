am4core.ready(function() { 

    // Themes begin
    am4core.useTheme(am4themes_animated);
    // Themes end
    
    var chart = am4core.create("chartdiv", am4plugins_wordCloud.WordCloud);
    chart.fontFamily = "Courier New";
    var series = chart.series.push(new am4plugins_wordCloud.WordCloudSeries());
    series.randomness = 0.1;
    series.rotationThreshold = 0.5;
    
    series.data = tagcloud_series_data;
    
    series.dataFields.word = "tag";
    series.dataFields.url = "url";
    series.dataFields.count = "count";
    series.dataFields.value = "index";
    
    series.heatRules.push({
     "target": series.labels.template,
     "property": "fill",
    //  "min": am4core.color("#0aa67b"),
    //  "max": am4core.color("#e2ff84"),
     "min": am4core.color("#fff"),
     "max": am4core.color("#fff"),
    "dataField": "value"
    });
    
    series.labels.template.url = tagcloud_url_root+"{url}";
    series.labels.template.urlTarget = "_self";
    series.labels.template.tooltipText = "{word}: {count}";
    series.labels.template.tooltip.fill = am4core.color("#000000");
    
    var hoverState = series.labels.template.states.create("hover");
    hoverState.properties.fill = am4core.color("#FF0000");
    
    // var subtitle = chart.titles.create();
    // subtitle.text = "(click to open)";
    
    var title = chart.titles.create();
    title.text = "Теги";
    title.fontSize = 20;
    title.fontWeight = "800";
    
    }); // end am4core.ready()