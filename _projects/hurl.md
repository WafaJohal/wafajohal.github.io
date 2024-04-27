---
layout: page
title: project 1
description: with background image
img: assets/img/12.jpg
importance: 1
category: work
related_publications: true
---


Robots are foreseen to be used in a variety of home contexts and interacting with novice users, such as assisting the dependent elderly in daily housework (i.e., caring and unpacking groceries, fetching, and pouring a glass of water, etc). Enabling robots to adapt to their environment through learning context specific tasks would be necessary for them to be used adequately by non-programming users.  

Several methods have been proposed to teach new skills to robots while keeping the human in the loop. Among these methods, the Reinforcement Learning (“RL”) approach is the most common one. However, the literature reports several issues with including human trainers in RL scenarios. Significant research reports a positive bias in RL rewards, and that human-generated reward signals change as the learning progress being inconsistent over time (the trainer adapts her strategy). This can be explained by the difficulty for human trainers to teach basic procedural motions. They generally tend to exaggerate their demonstrations or be more kind with time.  

In education, a good instructor maintains a mental model of the learner’s state (what has been learned and what needs clarification). This helps the teacher to appropriately structure the upcoming learning tasks with timely feedback and guidance. The learner can help the instructor by expressing their internal state via communicative acts that reveal their understanding, confusion, and attention. Robot’s learning parameters, however, can be overwhelming for a novice user and may increase the human workload (by increasing inaccurate feedbacks, and hence decreasing the robot’s learning). The challenge lies on training humans to be efficient trainers and enabling them to plan, assess and manage the robot’s learning.  

Another noticeable issue is the disengagement of humans during the training task. Teaching procedural skills to a robot learner can be time consuming and repetitive. This often results in increased noise in human feedback making their input less reliable. Some researchers have imagined several strategies for the robot to cope with this, such as detecting inconsistencies and asking for additional feedback. This project proposes to investigate how collaborative and competitive games could enable better quality feedback when robots are learning from humans. Inspired by instructional design, we will study how building teaching tools for human teachers can effectively improve the robot’s learning. We will also aim to engage the trainer longer by identifying and integrating a gamification element in the training.  

 This project is a 3-year endeavour funded by the Australian Research Council starting mid-2021. Under this umbrella, we are looking at hiring two PhD students in the Faculty of Engineering at the School of Computer Science. This project will make an extensive use of the National Facility for Human Robot Interaction Research.



<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/1.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/3.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/5.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Caption photos easily. On the left, a road goes through a tunnel. Middle, leaves artistically fall in a hipster photoshoot. Right, in another hipster photoshoot, a lumberjack grasps a handful of pine needles.
</div>
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/5.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    This image can also have a caption. It's like magic.
</div>

You can also put regular text between your rows of images, even citations {% cite einstein1950meaning %}.
Say you wanted to write a bit about your project before you posted the rest of the images.
You describe how you toiled, sweated, _bled_ for your project, and then... you reveal its glory in the next row of images.

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/6.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.liquid path="assets/img/11.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    You can also have artistically styled 2/3 + 1/3 images, like these.
</div>

The code is simple.
Just wrap your images with `<div class="col-sm">` and place them inside `<div class="row">` (read more about the <a href="https://getbootstrap.com/docs/4.4/layout/grid/">Bootstrap Grid</a> system).
To make images responsive, add `img-fluid` class to each; for rounded corners and shadows use `rounded` and `z-depth-1` classes.
Here's the code for the last row of images above:

{% raw %}

{% endraw %}