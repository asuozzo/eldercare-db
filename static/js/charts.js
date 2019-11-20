var draw = function(){
var svg = d3.select("#year-chart"),
  margin = {top: 20, right: 20, bottom: 30, left: 35},
  width = parseInt(svg.style('width')) - margin.left - margin.right,
  height = +svg.attr("height") - margin.top - margin.bottom;

svg.selectAll("*").remove();

// this range should actually come from the database
var start = new Date('January 1, 2014').getFullYear();
var end = new Date().getFullYear();
var years = Array();
for(i = start; i <= end; i++){years.push(i)};

var keys=["L","K","J","I","H","G","F","E","D","C","B","A"]

// reshape json
var data = []
years.forEach(function(y){
var d = {}
d["year"] = y;
// set 0 default for each level
keys.forEach(function(k){
  d[k]=0;
})
d["total"] = 0;
citations.forEach(function(c){
  if (String(c.year)==String(y)){
    d[c.severity_scope__letter] = c.severity_scope__letter__count;
  }
})
data.push(d);
})

data.forEach(function(d){
var year = d["year"]
citation_totals.forEach(function(i){
  if (i.year == year){
    d["total"] = i.severity_scope__count;
  }
})
return d;
})


g = svg.append("g").attr("transform", "translate(" + margin.left + "," +
                       margin.top + ")");

var y = d3.scaleBand()
  .rangeRound([0, height])
  .paddingInner(0.05)
  .align(0.1);

var x = d3.scaleLinear()
  .rangeRound([0, width]);

var z = d3.scaleOrdinal()
  .range([
    "#a51b02", "#a51b02", "#a51b02",
    "#b84326", "#b84326", "#b84326",
    "#d8836a","#d8836a","#d8836a",
    "#ded9d7","#ded9d7","#ded9d7"
    ]);

  y.domain(data.map(function(d) { return d.year; }));
  x.domain([0, d3.max(data, function(d) {return d.total;})]).nice();
  z.domain(keys);

var bars = g.append("g")
.selectAll("g")
.data(d3.stack().keys(keys)(data))
.enter().append("g")

bars.attr("fill", function(d) { return z(d.key); })
  .selectAll("rect")
  .data(function(d) { return d; })
  .enter().append("rect")
    .attr("class","bars")
    .attr("y", function(d) { return y(d.data.year); })
    .attr("x", function(d) {
        return x(d[0]); })
    .attr("width", function(d) { return x(d[1]) - x(d[0]); })
    .attr("height", y.bandwidth());

var text = g.append("g")
  .selectAll("text")
  .data(data)
  .enter()
  .append("text")
  .attr("x",function(d){
  return x(d.total)+5
})
  .attr("y",function(d){
  return y(d.year)+y.bandwidth()/2+6
})
  .text(function(d){
  if (d.total>0){
    return d.total
  } else {
    return ""
  }

})


g.append("g")
  .attr("class", "axis")
  .attr("transform", "translate(0,0)")
  .call(d3.axisLeft(y));
}

d3.select(window).on('resize', draw);
draw();

var scores = []
scoresList.forEach(function(d){
scores.push({"value":d});
})


var scoreSvg = d3.select("#facilityScores")
var drawScoreChart = function(){
var margin = {top: 40, right: 20, bottom: 40, left: 20},
height = scoreSvg.attr("height") - margin.top - margin.bottom;

var max = d3.max(scores, function(d){return d.value;});
var colorScale = d3.scaleLinear().domain([0,max]).range(['#fff9f7', '#a51b02']);
scoreSvg.selectAll(".chart-content").remove();
var width = parseInt(scoreSvg.style('width')) - margin.left - margin.right;
var x = d3.scaleLinear()
  .rangeRound([0, width]);

var g = scoreSvg.append("g")
.attr("class","chart-content")
.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var axis = g.append("g")
.attr("class","axis")
axis.append("line")
.attr("x2",0)
.attr("y1",height+margin.top/2+10)
.attr("x1",20)
.attr("y2",height+margin.top/2+10)
.attr("stroke","#000")
.attr("stroke-width",1.5)
.attr("marker-end","url(#arrow)");
axis.append("text")
.text("Better")
.attr("x",25)
.attr("y",height+margin.top/2+13)

axis.append("line")
.attr("x2",width)
.attr("y1",height+margin.top/2+10)
.attr("x1",width-20)
.attr("y2",height+margin.top/2+10)
.attr("stroke","#000")
.attr("stroke-width",1.5)
.attr("marker-end","url(#arrow)");
axis.append("text")
.text("Worse")
.attr("x",width-53)
.attr("y",height+margin.top/2+13)

x.domain(d3.extent(scores, function(d) { return d.value; }));

g.append("line")
.attr("x1", function(d){return x(score)})
.attr("y1", -30)
.attr("x2", function(d){return x(score)})
.attr("y2", height+20)
.attr("class","annotation")

g.append("text")
.attr("x", function(d){
if (score>(max/2)){
  return x(score) - 110;
} else {
  return x(score) + 5;
}}).attr("y",-20)
.text("This facility is here")

var simulation = d3.forceSimulation(scores)
  .force("x", d3.forceX(function(d) { return x(d.value); }).strength(.5))
  .force("y", d3.forceY(height / 2))
  .force("collide", d3.forceCollide(4))
  .stop();


for (var i = 0; i < 120; ++i) simulation.tick();

var cell = g.append("g")
  .attr("class", "cells")
.selectAll("g").data(d3.voronoi()
    .extent([[-margin.left, -margin.top], [width + margin.right, height + margin.top]])
    .x(function(d) { return d.x; })
    .y(function(d) { return d.y; })
  .polygons(scores)).enter().append("g");

cell.append("circle")
  .attr("r", 3.5)
  .attr("cx", function(d) { return d.data.x; })
  .attr("cy", function(d) {
return d.data.y; })
.style("fill",function(d){
return colorScale(d.data.value);
}).style(
  "stroke","lightgray"
);

cell.append("path")
  .attr("d", function(d) { return "M" + d.join("L") + "Z"; });
}

var drawCharts = function(){
draw();
drawScoreChart();
}

d3.select(window).on('resize', drawCharts);
drawCharts();


// map setup
mapboxgl.accessToken =
    'pk.eyJ1Ijoic2V2ZW5kYXlzIiwiYSI6ImNrMXM3aTg0azA5YTgzbW8wbmcyY3MzZ2gifQ.BRHRdBxzm9kdnwf3NTiwwQ';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/light-v10',
    center: coords,
    zoom: 9
});

map.scrollZoom.disable();

new mapboxgl.Marker()
    .setLngLat(coords)
    .addTo(map);