# reinforcement-learning

<a href="dds-pandemic-control.com">
<img  src="/static/assets/img/capture.JPG" alt="My cool logo"/>
</a>

Install
========

Install the virtualenv package

`pip install virtualenv`

Create virtual environment called env, myenv, etc. 

`virtualenv env`

Activate the virtualenvironmnent (LInux)

`source env/bin/activate`

Go the path of the project and install the required libraries 

`pip install -r requirements.txt`

Testing
-----------------
To run the server in the localhost run 

`python manage.py runserver`

Open your browser in the address localhost:8000 


File Description
-----------------
`project_emec2.py`: Takes input from the reinforcement learning model and creates the necessary JSON files for further visualization.

`manage.py`: Contains all the commands required to run the server

`requirements.txt`: Contains all library requirements to run the server

`articles\functions.py`: Contains general functions used by other scripts in the repository.

`articles\templates\welcome.html`: Contains Javascript and HTML scripts required for creating the dashboard

`static\data\RL Model`: Contains scripts for the reinfocement learning model



<!DOCTYPE html>
<html>
<head><meta charset="utf-8" />

<title>RL_Corona_30032021</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>



<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[75]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># !pip install tensorflow==2.3.0</span>
<span class="c1"># !pip install keras</span>
<span class="c1"># !pip install keras-rl2</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[98]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#Inputs</span>
<span class="n">s</span> <span class="o">=</span> <span class="mi">200</span> <span class="c1">#size of the grid</span>
<span class="n">N</span> <span class="o">=</span> <span class="mi">1000</span> <span class="c1">#size of population</span>
<span class="n">M</span> <span class="o">=</span> <span class="nb">round</span><span class="p">(</span><span class="n">N</span> <span class="o">*</span> <span class="mf">0.007</span><span class="p">)</span> <span class="c1">#Number of infectious population</span>
<span class="n">Et</span> <span class="o">=</span> <span class="mi">2</span> <span class="c1">#Number of days staying exposed</span>
<span class="n">It</span> <span class="o">=</span> <span class="mi">21</span> <span class="c1">#Number of days staying infectious</span>
<span class="n">Mt</span> <span class="o">=</span> <span class="mi">8</span> <span class="c1">#Number of daily movements</span>
<span class="n">D</span> <span class="o">=</span> <span class="mi">100</span> <span class="c1">#Number of days</span>
<span class="n">death_rate</span> <span class="o">=</span> <span class="mi">100</span>
<span class="n">expose_rate</span> <span class="o">=</span> <span class="mi">10</span>

<span class="c1">#Initialization</span>
<span class="n">S</span> <span class="o">=</span> <span class="n">N</span> <span class="o">-</span> <span class="n">M</span> <span class="c1">#Susceptible population</span>
<span class="n">E</span> <span class="o">=</span> <span class="mi">0</span> <span class="c1">#Exposed population</span>
<span class="n">I</span> <span class="o">=</span> <span class="n">M</span> <span class="c1">#Number of infectious population </span>
<span class="n">R</span> <span class="o">=</span> <span class="mi">0</span> <span class="c1">#Recovered population</span>
<span class="n">P</span> <span class="o">=</span> <span class="n">S</span> <span class="o">+</span> <span class="n">E</span> <span class="o">+</span> <span class="n">I</span> <span class="o">+</span> <span class="n">R</span> <span class="c1">#Total population</span>
<span class="n">economy</span> <span class="o">=</span> <span class="mi">0</span> <span class="c1">#Daily economic transaction</span>

<span class="n">policy_match</span> <span class="o">=</span> <span class="p">{</span><span class="mi">0</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">:</span><span class="mf">0.75</span><span class="p">,</span> <span class="mi">2</span><span class="p">:</span><span class="mf">0.25</span><span class="p">}</span> <span class="c1"># assign action to policy</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[99]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">gym</span> <span class="k">import</span> <span class="n">Env</span>
<span class="kn">from</span> <span class="nn">gym.spaces</span> <span class="k">import</span> <span class="n">Discrete</span><span class="p">,</span> <span class="n">Box</span><span class="p">,</span> <span class="n">Dict</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">random</span> 
<span class="kn">import</span> <span class="nn">time</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[108]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Create a virtual environment actions</span>
<span class="k">def</span> <span class="nf">reset</span><span class="p">():</span>
    <span class="k">global</span> <span class="n">P</span><span class="p">,</span> <span class="n">M</span><span class="p">,</span> <span class="n">It</span><span class="p">,</span> <span class="n">s</span>
    <span class="n">dummy_array</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">(</span><span class="n">shape</span><span class="o">=</span><span class="p">(</span><span class="n">P</span><span class="p">,</span><span class="mi">8</span><span class="p">))</span>
    <span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">dummy_array</span><span class="p">,</span><span class="n">columns</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;x&#39;</span><span class="p">,</span><span class="s1">&#39;y&#39;</span><span class="p">,</span><span class="s1">&#39;Day&#39;</span><span class="p">,</span><span class="s1">&#39;Susceptible&#39;</span><span class="p">,</span><span class="s1">&#39;Exposed&#39;</span><span class="p">,</span><span class="s1">&#39;Infectious&#39;</span><span class="p">,</span><span class="s1">&#39;Recovered&#39;</span><span class="p">,</span><span class="s1">&#39;GG&#39;</span><span class="p">])</span>
    <span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">astype</span><span class="p">({</span><span class="s1">&#39;x&#39;</span><span class="p">:</span><span class="nb">int</span><span class="p">,</span><span class="s1">&#39;y&#39;</span><span class="p">:</span><span class="nb">int</span><span class="p">,</span><span class="s1">&#39;Day&#39;</span><span class="p">:</span><span class="nb">int</span><span class="p">,</span><span class="s1">&#39;Susceptible&#39;</span><span class="p">:</span><span class="nb">bool</span><span class="p">,</span><span class="s1">&#39;Exposed&#39;</span><span class="p">:</span><span class="nb">int</span><span class="p">,</span><span class="s1">&#39;Infectious&#39;</span><span class="p">:</span><span class="nb">int</span><span class="p">,</span><span class="s1">&#39;Recovered&#39;</span><span class="p">:</span><span class="nb">bool</span><span class="p">,</span><span class="s1">&#39;GG&#39;</span><span class="p">:</span><span class="nb">bool</span><span class="p">})</span>
    <span class="n">df</span><span class="p">[</span><span class="s1">&#39;Susceptible&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span>
    <span class="c1">#Appending infectious population in </span>
    <span class="n">dfupdate</span><span class="o">=</span><span class="n">df</span><span class="o">.</span><span class="n">sample</span><span class="p">(</span><span class="n">M</span><span class="p">)</span>
    <span class="n">dfupdate</span><span class="p">[</span><span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="n">It</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="nb">len</span><span class="p">(</span><span class="n">dfupdate</span><span class="p">))</span>
    <span class="n">dfupdate</span><span class="p">[</span><span class="s1">&#39;Susceptible&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="kc">False</span>
    <span class="n">df</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="n">dfupdate</span><span class="p">)</span>
    <span class="n">update_list</span> <span class="o">=</span> <span class="n">dfupdate</span><span class="o">.</span><span class="n">index</span><span class="o">.</span><span class="n">tolist</span><span class="p">()</span> 
    <span class="c1">#Dispersing people randomly among grid</span>
    <span class="n">df</span><span class="p">[</span><span class="s1">&#39;x&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="n">s</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="p">))</span>
    <span class="n">df</span><span class="p">[</span><span class="s1">&#39;y&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">random</span><span class="o">.</span><span class="n">randint</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="n">s</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="p">))</span>

    <span class="k">return</span> <span class="n">df</span>

<span class="k">def</span> <span class="nf">update_pos</span><span class="p">(</span><span class="n">p</span><span class="p">,</span> <span class="n">df</span><span class="p">):</span>
    <span class="k">global</span> <span class="n">S</span>
    <span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">p</span><span class="p">,</span><span class="s1">&#39;x&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="nb">min</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">p</span><span class="p">,</span><span class="s1">&#39;x&#39;</span><span class="p">]</span><span class="o">+</span><span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">)),</span><span class="n">s</span><span class="p">),</span><span class="mi">0</span><span class="p">)</span> <span class="c1">#make valid movements in the grid</span>
    <span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">p</span><span class="p">,</span><span class="s1">&#39;y&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="nb">min</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">p</span><span class="p">,</span><span class="s1">&#39;y&#39;</span><span class="p">]</span><span class="o">+</span><span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">)),</span><span class="n">s</span><span class="p">),</span><span class="mi">0</span><span class="p">)</span> 
    
<span class="k">def</span> <span class="nf">coor_around</span><span class="p">(</span><span class="n">p</span><span class="p">,</span> <span class="n">df</span><span class="p">):</span>
    <span class="k">return</span> <span class="p">[(</span><span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">p</span><span class="p">,</span> <span class="s1">&#39;x&#39;</span><span class="p">]</span> <span class="o">+</span> <span class="n">a</span><span class="p">,</span> <span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">p</span><span class="p">,</span> <span class="s1">&#39;y&#39;</span><span class="p">]</span> <span class="o">+</span> <span class="n">b</span><span class="p">)</span> <span class="k">for</span> <span class="n">a</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">)</span> <span class="k">for</span> <span class="n">b</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">)]</span>

<span class="k">def</span> <span class="nf">one_day</span><span class="p">(</span><span class="n">df</span><span class="p">,</span> <span class="n">action</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span>
    <span class="c1"># start_time = time.time()</span>
    <span class="k">global</span> <span class="n">P</span><span class="p">,</span> <span class="n">M</span><span class="p">,</span> <span class="n">It</span><span class="p">,</span> <span class="n">S</span><span class="p">,</span> <span class="n">death_rate</span><span class="p">,</span> <span class="n">expose_rate</span>
    <span class="n">policy_match</span> <span class="o">=</span> <span class="p">{</span><span class="mi">0</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">:</span> <span class="mf">0.75</span><span class="p">,</span> <span class="mi">2</span><span class="p">:</span> <span class="mf">0.25</span><span class="p">}</span>  <span class="c1"># assign action to policy</span>
    <span class="n">moves_under_policy</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="nb">round</span><span class="p">(</span><span class="n">Mt</span> <span class="o">*</span> <span class="n">policy_match</span><span class="p">[</span><span class="n">action</span><span class="p">],</span> <span class="mi">0</span><span class="p">))</span>

    <span class="n">df_infectious</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[(</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">)]</span>
    <span class="n">df_infectious</span> <span class="o">=</span> <span class="n">df_infectious</span><span class="p">[[</span><span class="s1">&#39;x&#39;</span><span class="p">,</span> <span class="s1">&#39;y&#39;</span><span class="p">]]</span>

    <span class="k">for</span> <span class="n">mt</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">moves_under_policy</span><span class="p">):</span>
        <span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">person</span> <span class="ow">in</span> <span class="n">df</span><span class="o">.</span><span class="n">iterrows</span><span class="p">():</span>

            <span class="k">if</span> <span class="ow">not</span> <span class="n">person</span><span class="p">[</span><span class="s1">&#39;GG&#39;</span><span class="p">]:</span>  <span class="c1"># If the person is not dead</span>

                <span class="n">new_move_x</span> <span class="o">=</span> <span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">))</span>
                <span class="n">new_move_y</span> <span class="o">=</span> <span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">))</span>

                <span class="n">person</span><span class="p">[</span><span class="s1">&#39;x&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="nb">min</span><span class="p">(</span><span class="n">person</span><span class="p">[</span><span class="s1">&#39;x&#39;</span><span class="p">]</span> <span class="o">+</span> <span class="n">new_move_x</span><span class="p">,</span> <span class="n">s</span><span class="p">),</span> <span class="mi">0</span><span class="p">)</span>
                <span class="n">person</span><span class="p">[</span><span class="s1">&#39;y&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="nb">min</span><span class="p">(</span><span class="n">person</span><span class="p">[</span><span class="s1">&#39;y&#39;</span><span class="p">]</span> <span class="o">+</span> <span class="n">new_move_y</span><span class="p">,</span> <span class="n">s</span><span class="p">),</span> <span class="mi">0</span><span class="p">)</span>

                <span class="n">df</span><span class="o">.</span><span class="n">iat</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">person</span><span class="p">[</span><span class="s1">&#39;x&#39;</span><span class="p">])</span>
                <span class="n">df</span><span class="o">.</span><span class="n">iat</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">person</span><span class="p">[</span><span class="s1">&#39;y&#39;</span><span class="p">])</span>

                <span class="k">if</span> <span class="n">index</span> <span class="ow">in</span> <span class="n">df_infectious</span><span class="o">.</span><span class="n">index</span><span class="p">:</span>  <span class="c1"># assigning whats in person (row) to df_infectious at the correct index</span>
                    <span class="n">df_infectious</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="s1">&#39;x&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">person</span><span class="p">[</span><span class="s1">&#39;x&#39;</span><span class="p">]</span>
                    <span class="n">df_infectious</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="s1">&#39;y&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">person</span><span class="p">[</span><span class="s1">&#39;y&#39;</span><span class="p">]</span>

                <span class="k">if</span> <span class="p">(</span><span class="n">person</span><span class="p">[</span><span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">)</span> <span class="ow">and</span> <span class="p">(</span><span class="n">person</span><span class="p">[</span><span class="s1">&#39;Recovered&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="kc">False</span><span class="p">):</span>  <span class="c1"># If a person is in infectious state</span>
                    <span class="k">if</span> <span class="n">person</span><span class="p">[</span><span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">-</span> <span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">7</span><span class="p">))</span> <span class="o">&gt;=</span> <span class="n">It</span><span class="p">:</span>  <span class="c1"># If the infectious days are completed</span>
                        <span class="k">if</span> <span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">death_rate</span><span class="p">))</span> <span class="o">&gt;</span> <span class="p">(</span>
                                <span class="n">death_rate</span> <span class="o">-</span> <span class="mi">2</span><span class="p">):</span>  <span class="c1"># If the person dies(with probability distribution 1:4)</span>
                            <span class="n">df</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span>
                            <span class="k">if</span> <span class="n">index</span> <span class="ow">in</span> <span class="n">df_infectious</span><span class="o">.</span><span class="n">index</span><span class="p">:</span>
                                <span class="n">df_infectious</span><span class="o">.</span><span class="n">drop</span><span class="p">([</span><span class="n">index</span><span class="p">])</span>

                            <span class="n">df</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="s1">&#39;GG&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span>  <span class="c1"># Kill the person</span>
                        <span class="k">else</span><span class="p">:</span>  <span class="c1"># If the person survives</span>
                            <span class="n">df</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span>
                            <span class="k">if</span> <span class="n">index</span> <span class="ow">in</span> <span class="n">df_infectious</span><span class="o">.</span><span class="n">index</span><span class="p">:</span>
                                <span class="n">df_infectious</span><span class="o">.</span><span class="n">drop</span><span class="p">([</span><span class="n">index</span><span class="p">])</span>
                            <span class="n">df</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="s1">&#39;Recovered&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="kc">True</span>  <span class="c1"># Recover the person</span>
                    <span class="k">elif</span> <span class="n">mt</span> <span class="o">+</span> <span class="mi">1</span> <span class="o">==</span> <span class="n">moves_under_policy</span><span class="p">:</span>
                        <span class="k">if</span> <span class="n">person</span><span class="p">[</span><span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="mf">0.5</span><span class="p">:</span>
                            <span class="n">df</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>
                        <span class="k">else</span><span class="p">:</span>
                            <span class="n">df</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">person</span><span class="p">[</span><span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">+</span> <span class="mi">1</span>  <span class="c1"># Increase the infectious day counter   </span>
        
                
                <span class="k">elif</span> <span class="n">person</span><span class="p">[</span><span class="s1">&#39;Exposed&#39;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>  <span class="c1"># If a person is in exposed state</span>
                    
                    <span class="k">if</span> <span class="p">(</span><span class="n">person</span><span class="p">[</span><span class="s1">&#39;Exposed&#39;</span><span class="p">]</span> <span class="o">-</span> <span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">10</span><span class="p">)))</span> <span class="o">&gt;=</span> <span class="n">Et</span><span class="p">:</span>  <span class="c1"># If the person has reached the exposed day limit?  7</span>
                        
                        <span class="n">df</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="s1">&#39;Exposed&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span>
                        <span class="n">df</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mf">0.5</span> <span class="k">if</span> <span class="n">mt</span><span class="o">+</span><span class="mi">1</span> <span class="o">!=</span> <span class="n">moves_under_policy</span> <span class="k">else</span> <span class="mi">1</span>  <span class="c1"># Increase the infectious day counter, now the person is infectious</span>
                        <span class="n">df_infectious</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">person</span><span class="p">)</span>
                    <span class="k">elif</span> <span class="n">mt</span> <span class="o">+</span> <span class="mi">1</span> <span class="o">==</span> <span class="n">moves_under_policy</span><span class="p">:</span> <span class="c1"># At the end of the day</span>
                        <span class="k">if</span> <span class="n">person</span><span class="p">[</span><span class="s1">&#39;Exposed&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="mf">0.5</span><span class="p">:</span>
                            <span class="n">df</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="s1">&#39;Exposed&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>
                        <span class="k">else</span><span class="p">:</span>
                            <span class="n">df</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="s1">&#39;Exposed&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">person</span><span class="p">[</span><span class="s1">&#39;Exposed&#39;</span><span class="p">]</span> <span class="o">+</span> <span class="mi">1</span>  <span class="c1"># Increase the exposed day counter</span>
                        
                <span class="k">elif</span> <span class="n">person</span><span class="p">[</span><span class="s1">&#39;Susceptible&#39;</span><span class="p">]:</span>  <span class="c1"># If the person is in susceptible state</span>

                    <span class="n">x_temp</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">person</span><span class="p">[</span><span class="s1">&#39;x&#39;</span><span class="p">])</span>
                    <span class="n">df_xtemp</span> <span class="o">=</span> <span class="n">df_infectious</span><span class="p">[[</span><span class="s1">&#39;x&#39;</span><span class="p">]]</span><span class="o">.</span><span class="n">to_numpy</span><span class="p">()</span>

                    <span class="k">if</span> <span class="p">(</span><span class="n">x_temp</span> <span class="ow">in</span> <span class="n">df_xtemp</span><span class="p">)</span> <span class="ow">or</span> <span class="p">((</span><span class="n">x_temp</span> <span class="o">-</span> <span class="mi">1</span><span class="p">)</span> <span class="ow">in</span> <span class="n">df_xtemp</span><span class="p">)</span> <span class="ow">or</span> <span class="p">((</span><span class="n">x_temp</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span> <span class="ow">in</span> <span class="n">df_xtemp</span><span class="p">):</span>

                        <span class="n">y_temp</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">person</span><span class="p">[</span><span class="s1">&#39;y&#39;</span><span class="p">])</span>
                        <span class="n">df_ytemp</span> <span class="o">=</span> <span class="n">df_infectious</span><span class="p">[[</span><span class="s1">&#39;y&#39;</span><span class="p">]]</span><span class="o">.</span><span class="n">to_numpy</span><span class="p">()</span>
                        <span class="k">if</span> <span class="p">(</span><span class="n">y_temp</span> <span class="ow">in</span> <span class="n">df_ytemp</span><span class="p">)</span> <span class="ow">or</span> <span class="p">((</span><span class="n">y_temp</span> <span class="o">-</span> <span class="mi">1</span><span class="p">)</span> <span class="ow">in</span> <span class="n">df_ytemp</span><span class="p">)</span> <span class="ow">or</span> <span class="p">((</span><span class="n">y_temp</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span> <span class="ow">in</span> <span class="n">df_ytemp</span><span class="p">):</span>
                            <span class="k">if</span> <span class="n">random</span><span class="o">.</span><span class="n">choice</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="n">expose_rate</span><span class="p">))</span> <span class="o">&gt;</span> <span class="p">(</span><span class="n">expose_rate</span> <span class="o">-</span> <span class="mi">2</span><span class="p">):</span>
                                <span class="n">df</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="s1">&#39;Exposed&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mf">0.5</span> <span class="k">if</span> <span class="n">mt</span><span class="o">+</span><span class="mi">1</span> <span class="o">!=</span> <span class="n">moves_under_policy</span> <span class="k">else</span> <span class="mi">1</span>
                                <span class="n">df</span><span class="o">.</span><span class="n">at</span><span class="p">[</span><span class="n">index</span><span class="p">,</span> <span class="s1">&#39;Susceptible&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="kc">False</span>
                                
                    
    <span class="c1"># print(&quot;--- %s seconds ---&quot; % (time.time() - start_time))</span>

    <span class="k">return</span> <span class="n">df</span>  <span class="c1"># time.time() - start_time #</span>

<span class="k">def</span> <span class="nf">economy_gain</span><span class="p">(</span><span class="n">df</span><span class="p">):</span>
    <span class="n">economy_gain</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="p">[(</span><span class="n">df</span><span class="o">.</span><span class="n">GG</span> <span class="o">==</span> <span class="kc">False</span><span class="p">)</span> <span class="o">&amp;</span> <span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">Infectious</span> <span class="o">==</span> <span class="mi">0</span><span class="p">)])</span> <span class="o">*</span> <span class="nb">round</span><span class="p">(</span><span class="n">random</span><span class="o">.</span><span class="n">uniform</span><span class="p">(</span><span class="mf">0.8</span><span class="p">,</span><span class="mi">1</span><span class="p">),</span> <span class="mi">2</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">economy_gain</span>

<span class="k">def</span> <span class="nf">current_state</span><span class="p">(</span><span class="n">df</span><span class="p">):</span>
    <span class="k">global</span> <span class="n">economy</span>
    <span class="n">active_cases</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">])</span>
    <span class="n">new_inf</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="mi">1</span><span class="p">])</span>
    <span class="n">recovered</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Recovered&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="kc">True</span><span class="p">])</span>
    <span class="n">gg</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;GG&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="kc">True</span><span class="p">])</span>
    <span class="n">reproduction_rate</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="mi">1</span><span class="p">])</span> <span class="o">/</span> <span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">])</span> <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s1">&#39;Infectious&#39;</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">])</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="k">else</span> <span class="mi">0</span>
    <span class="n">economy</span> <span class="o">=</span> <span class="n">economy</span> <span class="o">+</span> <span class="n">economy_gain</span><span class="p">(</span><span class="n">df</span><span class="p">)</span>
        
    <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="n">active_cases</span><span class="p">,</span> <span class="n">new_inf</span><span class="p">,</span> <span class="n">recovered</span><span class="p">,</span> <span class="n">gg</span><span class="p">,</span> <span class="n">reproduction_rate</span><span class="p">,</span> <span class="n">economy</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[109]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">simulation</span><span class="p">():</span>
    <span class="n">df</span> <span class="o">=</span> <span class="n">reset</span><span class="p">()</span>
    <span class="n">states</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">df_collect</span> <span class="o">=</span> <span class="n">df</span>
    <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">5</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">d</span><span class="p">)</span>
        <span class="n">df</span> <span class="o">=</span> <span class="n">one_day</span><span class="p">(</span><span class="n">df</span><span class="p">)</span>
        <span class="n">df</span><span class="o">.</span><span class="n">Day</span> <span class="o">=</span> <span class="n">d</span><span class="o">+</span><span class="mi">1</span>
        <span class="n">df_collect</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">concat</span><span class="p">([</span><span class="n">df_collect</span><span class="p">,</span> <span class="n">df</span><span class="p">])</span>
        <span class="n">states</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">current_state</span><span class="p">(</span><span class="n">df</span><span class="p">))</span>
    <span class="k">return</span> <span class="n">df_collect</span><span class="p">,</span> <span class="n">states</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[110]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">def_observation_space</span> <span class="o">=</span> <span class="n">Box</span><span class="p">(</span><span class="n">low</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">]),</span> <span class="n">high</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span><span class="n">P</span><span class="p">,</span><span class="n">P</span><span class="p">,</span><span class="n">P</span><span class="p">,</span><span class="n">P</span><span class="p">,</span><span class="mi">10</span><span class="p">,</span><span class="n">P</span><span class="o">*</span><span class="n">D</span><span class="o">*</span><span class="n">Mt</span><span class="p">],</span> <span class="n">dtype</span> <span class="o">=</span> <span class="nb">int</span><span class="p">))</span>
<span class="c1">##[active_cases, new_inf, recovered, gg, reproduction_rate, economy]</span>

<span class="c1"># Create the virtual environment for RL</span>
<span class="k">class</span> <span class="nc">CoronaPolicy</span><span class="p">(</span><span class="n">Env</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">action_space</span> <span class="o">=</span> <span class="n">Discrete</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
        
        <span class="bp">self</span><span class="o">.</span><span class="n">observation_space</span> <span class="o">=</span> <span class="n">def_observation_space</span> <span class="c1"># Box(low = 0, high = P, shape = (5,1), dtype = int )</span>
        <span class="c1"># Dict(recovered=Discrete(P+1), sus=Discrete(P+1), exposed=Discrete(P+1),inf=Discrete(P+1),gg=Discrete(P+1))</span>
        
        <span class="bp">self</span><span class="o">.</span><span class="n">df</span> <span class="o">=</span> <span class="n">reset</span><span class="p">()</span>
        
        <span class="bp">self</span><span class="o">.</span><span class="n">state</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">current_state</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">df</span><span class="p">))</span>
        
        <span class="bp">self</span><span class="o">.</span><span class="n">day</span> <span class="o">=</span> <span class="mi">0</span>
        
        
        
    <span class="k">def</span> <span class="nf">step</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">action</span><span class="p">):</span>
        
        <span class="bp">self</span><span class="o">.</span><span class="n">df</span> <span class="o">=</span> <span class="n">one_day</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">df</span><span class="p">,</span> <span class="n">action</span><span class="p">)</span>
        
        <span class="bp">self</span><span class="o">.</span><span class="n">state</span> <span class="o">=</span> <span class="n">current_state</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">df</span><span class="p">)</span>
        
        <span class="bp">self</span><span class="o">.</span><span class="n">day</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">day</span> <span class="o">+</span> <span class="mi">1</span>
        
        <span class="n">reward</span> <span class="o">=</span> <span class="n">economy_gain</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">df</span><span class="p">)</span>
        
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">day</span> <span class="o">&lt;=</span> <span class="n">D</span><span class="p">:</span>
            <span class="n">done</span> <span class="o">=</span> <span class="kc">False</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">done</span> <span class="o">=</span> <span class="kc">True</span>
            
        <span class="n">info</span> <span class="o">=</span> <span class="p">{}</span>
        
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">state</span><span class="p">,</span> <span class="n">reward</span><span class="p">,</span> <span class="n">done</span><span class="p">,</span> <span class="n">info</span>
    
    <span class="k">def</span> <span class="nf">render</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">pass</span>
    
    <span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">observation_space</span> <span class="o">=</span> <span class="n">def_observation_space</span>
        
        <span class="bp">self</span><span class="o">.</span><span class="n">df</span> <span class="o">=</span> <span class="n">reset</span><span class="p">()</span>
        
        <span class="bp">self</span><span class="o">.</span><span class="n">state</span> <span class="o">=</span> <span class="n">current_state</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">df</span><span class="p">)</span>
        
        <span class="bp">self</span><span class="o">.</span><span class="n">day</span> <span class="o">=</span> <span class="mi">0</span>
        
        
        
        
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">state</span>
        
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>/Users/yi/opt/anaconda3/lib/python3.7/site-packages/gym/logger.py:30: UserWarning: <span class="ansi-yellow-fg">WARN: Box bound precision lowered by casting to float32</span>
  warnings.warn(colorize(&#39;%s: %s&#39;%(&#39;WARN&#39;, msg % args), &#39;yellow&#39;))
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[111]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">env</span> <span class="o">=</span> <span class="n">CoronaPolicy</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[112]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># episodes = 10</span>
<span class="c1"># for episode in range(1, episodes+1):</span>
<span class="c1">#     state = env.reset()</span>
<span class="c1">#     done = False</span>
<span class="c1">#     economy = 0</span>
    
<span class="c1">#     while not done:</span>
<span class="c1">#         action = env.action_space.sample()</span>
<span class="c1">#         n_state, reward, done, info = env.step(action)</span>
<span class="c1">#         economy += reward</span>
        
<span class="c1">#     print(f&#39;Episode: {episode} Score: {economy}&#39;)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Deep-Learning-Model-with-Keras">Deep Learning Model with Keras<a class="anchor-link" href="#Deep-Learning-Model-with-Keras">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[113]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">tensorflow.keras.models</span> <span class="k">import</span> <span class="n">Sequential</span>
<span class="kn">from</span> <span class="nn">tensorflow.keras.layers</span> <span class="k">import</span> <span class="n">Dense</span><span class="p">,</span> <span class="n">Flatten</span>
<span class="kn">from</span> <span class="nn">tensorflow.keras.optimizers</span> <span class="k">import</span> <span class="n">Adam</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[114]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">build_model</span><span class="p">(</span><span class="n">states</span><span class="p">,</span> <span class="n">actions</span><span class="p">):</span>
    <span class="n">model</span> <span class="o">=</span> <span class="n">Sequential</span><span class="p">()</span>
    <span class="n">model</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Dense</span><span class="p">(</span><span class="mi">32</span><span class="p">,</span> <span class="n">activation</span> <span class="o">=</span> <span class="s1">&#39;relu&#39;</span><span class="p">,</span><span class="n">input_shape</span> <span class="o">=</span> <span class="n">states</span><span class="p">))</span>
    <span class="n">model</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Dense</span><span class="p">(</span><span class="mi">64</span><span class="p">,</span> <span class="n">activation</span> <span class="o">=</span> <span class="s1">&#39;relu&#39;</span><span class="p">))</span>
    <span class="n">model</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">Dense</span><span class="p">(</span><span class="n">actions</span><span class="p">,</span> <span class="n">activation</span> <span class="o">=</span> <span class="s1">&#39;linear&#39;</span><span class="p">))</span>
    <span class="k">return</span> <span class="n">model</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[120]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># del model</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[121]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">states</span> <span class="o">=</span> <span class="n">env</span><span class="o">.</span><span class="n">observation_space</span><span class="o">.</span><span class="n">shape</span>
<span class="n">actions</span> <span class="o">=</span> <span class="n">env</span><span class="o">.</span><span class="n">action_space</span><span class="o">.</span><span class="n">n</span>
<span class="n">model</span> <span class="o">=</span> <span class="n">build_model</span><span class="p">(</span><span class="n">states</span><span class="p">,</span> <span class="n">actions</span><span class="p">)</span>
<span class="n">model</span><span class="o">.</span><span class="n">summary</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Model: &#34;sequential_1&#34;
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_3 (Dense)              (None, 32)                224       
_________________________________________________________________
dense_4 (Dense)              (None, 64)                2112      
_________________________________________________________________
dense_5 (Dense)              (None, 3)                 195       
=================================================================
Total params: 2,531
Trainable params: 2,531
Non-trainable params: 0
_________________________________________________________________
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Build-Agent-with-Keras-RL">Build Agent with Keras-RL<a class="anchor-link" href="#Build-Agent-with-Keras-RL">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[117]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">rl.agents</span> <span class="k">import</span> <span class="n">DQNAgent</span>
<span class="kn">from</span> <span class="nn">rl.policy</span> <span class="k">import</span> <span class="n">BoltzmannQPolicy</span>
<span class="kn">from</span> <span class="nn">rl.memory</span> <span class="k">import</span> <span class="n">SequentialMemory</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[122]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">build_agent</span><span class="p">(</span><span class="n">model</span><span class="p">,</span> <span class="n">actions</span><span class="p">):</span>
    <span class="n">policy</span> <span class="o">=</span> <span class="n">BoltzmannQPolicy</span><span class="p">()</span> <span class="c1"># ?</span>
    <span class="n">memory</span> <span class="o">=</span> <span class="n">SequentialMemory</span><span class="p">(</span><span class="n">limit</span> <span class="o">=</span> <span class="mi">1000</span><span class="p">,</span> <span class="n">window_length</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span>
    <span class="n">dqn</span> <span class="o">=</span> <span class="n">DQNAgent</span><span class="p">(</span><span class="n">model</span> <span class="o">=</span> <span class="n">model</span><span class="p">,</span> <span class="n">memory</span> <span class="o">=</span> <span class="n">memory</span><span class="p">,</span> <span class="n">policy</span> <span class="o">=</span> <span class="n">policy</span><span class="p">,</span> 
                   <span class="n">nb_actions</span> <span class="o">=</span> <span class="n">actions</span><span class="p">,</span> <span class="n">nb_steps_warmup</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span> <span class="n">target_model_update</span> <span class="o">=</span> <span class="mi">1000</span><span class="p">)</span> <span class="c1"># target_model_update</span>
                  
    <span class="k">return</span> <span class="n">dqn</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dqn</span> <span class="o">=</span> <span class="n">build_agent</span><span class="p">(</span><span class="n">model</span><span class="p">,</span> <span class="n">actions</span><span class="p">)</span>
<span class="n">dqn</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="n">Adam</span><span class="p">(</span><span class="n">lr</span> <span class="o">=</span> <span class="mf">1e-3</span><span class="p">),</span> <span class="n">metrics</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;mae&#39;</span><span class="p">])</span>
<span class="n">dqn</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">env</span><span class="p">,</span> <span class="n">nb_steps</span> <span class="o">=</span> <span class="mi">2000</span><span class="p">,</span> <span class="n">visualize</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span> <span class="n">verbose</span> <span class="o">=</span> <span class="mi">1</span>  <span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Training for 2000 steps ...
Interval 1 (0 steps performed)
WARNING:tensorflow:From /Users/yi/opt/anaconda3/lib/python3.7/site-packages/tensorflow/python/keras/engine/training_v1.py:2070: Model.state_updates (from tensorflow.python.keras.engine.training) is deprecated and will be removed in a future version.
Instructions for updating:
This property should not be used in TensorFlow 2.0, as updates are applied automatically.
No. 28 exposure increased to 1.0 in day 4 at 5
    1/10000 [..............................] - ETA: 53:06:12 - reward: 993.0000No. 28 exposure increased to 2.0 in day 4 at 1
No. 111 exposure increased to 1.0 in day 4 at 1
    2/10000 [..............................] - ETA: 35:03:16 - reward: 938.3850*When No. 28 infected, Exposure is 2.0 in day 4 at move 1
No. 111 exposure increased to 2.0 in day 4 at 5
No. 169 exposure increased to 1.0 in day 4 at 5
No. 558 exposure increased to 2.0 in day 4 at 5
No. 890 exposure increased to 1.0 in day 4 at 5
No. 937 exposure increased to 1.0 in day 4 at 5
    3/10000 [..............................] - ETA: 37:39:48 - reward: 946.6600No. 111 exposure increased to 3.0 in day 4 at 1
No. 169 exposure increased to 2.0 in day 4 at 1
No. 303 exposure increased to 2.0 in day 4 at 1
No. 442 exposure increased to 2.0 in day 4 at 1
No. 558 exposure increased to 3.0 in day 4 at 1
No. 890 exposure increased to 2.0 in day 4 at 1
No. 937 exposure increased to 2.0 in day 4 at 1
    4/10000 [..............................] - ETA: 31:40:00 - reward: 943.3500*When No. 890 infected, Exposure is 2.0 in day 4 at move 0
*When No. 303 infected, Exposure is 2.0 in day 4 at move 1
*When No. 558 infected, Exposure is 3.0 in day 4 at move 1
*When No. 442 infected, Exposure is 2.0 in day 4 at move 2
*When No. 169 infected, Exposure is 2.0 in day 4 at move 3
No. 61 exposure increased to 1.0 in day 4 at 5
No. 111 exposure increased to 4.0 in day 4 at 5
No. 872 exposure increased to 1.0 in day 4 at 5
No. 937 exposure increased to 3.0 in day 4 at 5
    5/10000 [..............................] - ETA: 34:32:29 - reward: 924.7880*When No. 111 infected, Exposure is 4.0 in day 4 at move 0
No. 61 exposure increased to 2.0 in day 4 at 1
No. 594 exposure increased to 1.0 in day 4 at 1
No. 608 exposure increased to 1.0 in day 4 at 1
No. 872 exposure increased to 2.0 in day 4 at 1
No. 937 exposure increased to 4.0 in day 4 at 1
    6/10000 [..............................] - ETA: 30:51:12 - reward: 904.0367*When No. 937 infected, Exposure is 4.0 in day 4 at move 0
No. 61 exposure increased to 3.0 in day 4 at 5
No. 110 exposure increased to 1.0 in day 4 at 5
No. 153 exposure increased to 1.0 in day 4 at 5
No. 259 exposure increased to 1.0 in day 4 at 5
No. 594 exposure increased to 2.0 in day 4 at 5
No. 608 exposure increased to 2.0 in day 4 at 5
No. 872 exposure increased to 3.0 in day 4 at 5
    7/10000 [..............................] - ETA: 32:32:10 - reward: 898.9686No. 61 exposure increased to 4.0 in day 4 at 5
No. 110 exposure increased to 2.0 in day 4 at 5
No. 153 exposure increased to 2.0 in day 4 at 5
No. 209 exposure increased to 1.0 in day 4 at 5
No. 259 exposure increased to 2.0 in day 4 at 5
No. 552 exposure increased to 1.0 in day 4 at 5
No. 594 exposure increased to 3.0 in day 4 at 5
No. 608 exposure increased to 3.0 in day 4 at 5
No. 627 exposure increased to 1.0 in day 4 at 5
No. 687 exposure increased to 2.0 in day 4 at 5
No. 872 exposure increased to 4.0 in day 4 at 5
    8/10000 [..............................] - ETA: 33:50:52 - reward: 899.0963*When No. 259 infected, Exposure is 2.0 in day 4 at move 0
*When No. 594 infected, Exposure is 3.0 in day 4 at move 0
*When No. 872 infected, Exposure is 4.0 in day 4 at move 0
*When No. 153 infected, Exposure is 2.0 in day 4 at move 2
No. 61 exposure increased to 5.0 in day 4 at 5
No. 92 exposure increased to 1.0 in day 4 at 5
No. 110 exposure increased to 3.0 in day 4 at 5
No. 122 exposure increased to 1.0 in day 4 at 5
No. 209 exposure increased to 2.0 in day 4 at 5
No. 298 exposure increased to 1.0 in day 4 at 5
No. 327 exposure increased to 1.0 in day 4 at 5
No. 527 exposure increased to 1.0 in day 4 at 5
No. 552 exposure increased to 2.0 in day 4 at 5
No. 608 exposure increased to 4.0 in day 4 at 5
No. 627 exposure increased to 2.0 in day 4 at 5
*When No. 687 infected, Exposure is 2.0 in day 4 at move 5
No. 725 exposure increased to 1.0 in day 4 at 5
    9/10000 [..............................] - ETA: 34:41:01 - reward: 893.2233*When No. 61 infected, Exposure is 5.0 in day 4 at move 0
No. 70 exposure increased to 1.0 in day 4 at 1
No. 92 exposure increased to 2.0 in day 4 at 1
No. 110 exposure increased to 4.0 in day 4 at 1
No. 122 exposure increased to 2.0 in day 4 at 1
No. 207 exposure increased to 2.0 in day 4 at 1
No. 209 exposure increased to 3.0 in day 4 at 1
No. 248 exposure increased to 2.0 in day 4 at 1
No. 298 exposure increased to 2.0 in day 4 at 1
No. 327 exposure increased to 2.0 in day 4 at 1
No. 411 exposure increased to 2.0 in day 4 at 1
No. 527 exposure increased to 2.0 in day 4 at 1
No. 552 exposure increased to 3.0 in day 4 at 1
No. 608 exposure increased to 5.0 in day 4 at 1
No. 627 exposure increased to 3.0 in day 4 at 1
No. 725 exposure increased to 2.0 in day 4 at 1
No. 846 exposure increased to 1.0 in day 4 at 1
No. 946 exposure increased to 2.0 in day 4 at 1
   10/10000 [..............................] - ETA: 32:36:29 - reward: 902.2010*When No. 608 infected, Exposure is 5.0 in day 4 at move 0
No. 19 exposure increased to 1.0 in day 4 at 1
No. 70 exposure increased to 2.0 in day 4 at 1
No. 92 exposure increased to 3.0 in day 4 at 1
No. 110 exposure increased to 5.0 in day 4 at 1
*When No. 122 infected, Exposure is 2.0 in day 4 at move 1
No. 207 exposure increased to 3.0 in day 4 at 1
No. 209 exposure increased to 4.0 in day 4 at 1
No. 210 exposure increased to 1.0 in day 4 at 1
No. 248 exposure increased to 3.0 in day 4 at 1
No. 298 exposure increased to 3.0 in day 4 at 1
No. 327 exposure increased to 3.0 in day 4 at 1
No. 411 exposure increased to 3.0 in day 4 at 1
No. 527 exposure increased to 3.0 in day 4 at 1
No. 550 exposure increased to 1.0 in day 4 at 1
No. 552 exposure increased to 4.0 in day 4 at 1
*When No. 627 infected, Exposure is 3.0 in day 4 at move 1
No. 725 exposure increased to 3.0 in day 4 at 1
No. 782 exposure increased to 1.0 in day 4 at 1
No. 846 exposure increased to 2.0 in day 4 at 1
No. 946 exposure increased to 3.0 in day 4 at 1
No. 985 exposure increased to 2.0 in day 4 at 1
   11/10000 [..............................] - ETA: 30:54:14 - reward: 903.9282*When No. 209 infected, Exposure is 4.0 in day 4 at move 0
*When No. 298 infected, Exposure is 3.0 in day 4 at move 0
*When No. 411 infected, Exposure is 3.0 in day 4 at move 0
No. 6 exposure increased to 1.0 in day 4 at 1
No. 19 exposure increased to 2.0 in day 4 at 1
No. 70 exposure increased to 3.0 in day 4 at 1
No. 92 exposure increased to 4.0 in day 4 at 1
*When No. 110 infected, Exposure is 5.0 in day 4 at move 1
No. 207 exposure increased to 4.0 in day 4 at 1
No. 210 exposure increased to 2.0 in day 4 at 1
No. 248 exposure increased to 4.0 in day 4 at 1
No. 327 exposure increased to 4.0 in day 4 at 1
No. 432 exposure increased to 1.0 in day 4 at 1
No. 527 exposure increased to 4.0 in day 4 at 1
No. 550 exposure increased to 2.0 in day 4 at 1
*When No. 552 infected, Exposure is 4.0 in day 4 at move 1
No. 620 exposure increased to 2.0 in day 4 at 1
*When No. 725 infected, Exposure is 3.0 in day 4 at move 1
No. 726 exposure increased to 2.0 in day 4 at 1
No. 747 exposure increased to 2.0 in day 4 at 1
No. 782 exposure increased to 2.0 in day 4 at 1
No. 812 exposure increased to 1.0 in day 4 at 1
No. 846 exposure increased to 3.0 in day 4 at 1
No. 946 exposure increased to 4.0 in day 4 at 1
No. 960 exposure increased to 1.0 in day 4 at 1
No. 985 exposure increased to 3.0 in day 4 at 1
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>/Users/yi/opt/anaconda3/lib/python3.7/site-packages/rl/memory.py:40: UserWarning: Not enough entries to sample without replacement. Consider increasing your warm-up phase to avoid oversampling!
  warnings.warn(&#39;Not enough entries to sample without replacement. Consider increasing your warm-up phase to avoid oversampling!&#39;)
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>   12/10000 [..............................] - ETA: 29:35:13 - reward: 907.3325*When No. 19 infected, Exposure is 2.0 in day 4 at move 0
No. 6 exposure increased to 2.0 in day 4 at 1
*When No. 70 infected, Exposure is 3.0 in day 4 at move 1
No. 92 exposure increased to 5.0 in day 4 at 1
No. 142 exposure increased to 2.0 in day 4 at 1
*When No. 207 infected, Exposure is 4.0 in day 4 at move 1
No. 210 exposure increased to 3.0 in day 4 at 1
No. 248 exposure increased to 5.0 in day 4 at 1
No. 327 exposure increased to 5.0 in day 4 at 1
No. 432 exposure increased to 2.0 in day 4 at 1
*When No. 527 infected, Exposure is 4.0 in day 4 at move 1
No. 550 exposure increased to 3.0 in day 4 at 1
No. 620 exposure increased to 3.0 in day 4 at 1
No. 623 exposure increased to 2.0 in day 4 at 1
No. 726 exposure increased to 3.0 in day 4 at 1
No. 747 exposure increased to 3.0 in day 4 at 1
No. 782 exposure increased to 3.0 in day 4 at 1
No. 812 exposure increased to 2.0 in day 4 at 1
No. 829 exposure increased to 1.0 in day 4 at 1
No. 846 exposure increased to 4.0 in day 4 at 1
No. 946 exposure increased to 5.0 in day 4 at 1
No. 960 exposure increased to 2.0 in day 4 at 1
No. 985 exposure increased to 4.0 in day 4 at 1
   13/10000 [..............................] - ETA: 28:31:17 - reward: 909.9146*When No. 248 infected, Exposure is 5.0 in day 4 at move 0
*When No. 620 infected, Exposure is 3.0 in day 4 at move 0
No. 6 exposure increased to 3.0 in day 4 at 1
No. 92 exposure increased to 6.0 in day 4 at 1
No. 107 exposure increased to 2.0 in day 4 at 1
No. 142 exposure increased to 3.0 in day 4 at 1
No. 144 exposure increased to 2.0 in day 4 at 1
No. 210 exposure increased to 4.0 in day 4 at 1
*When No. 327 infected, Exposure is 5.0 in day 4 at move 1
No. 371 exposure increased to 1.0 in day 4 at 1
No. 416 exposure increased to 1.0 in day 4 at 1
No. 432 exposure increased to 3.0 in day 4 at 1
No. 440 exposure increased to 2.0 in day 4 at 1
*When No. 550 infected, Exposure is 3.0 in day 4 at move 1
No. 576 exposure increased to 1.0 in day 4 at 1
No. 623 exposure increased to 3.0 in day 4 at 1
No. 726 exposure increased to 4.0 in day 4 at 1
No. 744 exposure increased to 2.0 in day 4 at 1
No. 747 exposure increased to 4.0 in day 4 at 1
No. 782 exposure increased to 4.0 in day 4 at 1
No. 810 exposure increased to 2.0 in day 4 at 1
No. 812 exposure increased to 3.0 in day 4 at 1
No. 829 exposure increased to 2.0 in day 4 at 1
No. 846 exposure increased to 5.0 in day 4 at 1
No. 946 exposure increased to 6.0 in day 4 at 1
No. 960 exposure increased to 3.0 in day 4 at 1
No. 971 exposure increased to 2.0 in day 4 at 1
No. 985 exposure increased to 5.0 in day 4 at 1
   14/10000 [..............................] - ETA: 27:38:21 - reward: 903.5707*When No. 210 infected, Exposure is 4.0 in day 4 at move 0
*When No. 623 infected, Exposure is 3.0 in day 4 at move 0
*When No. 782 infected, Exposure is 4.0 in day 4 at move 0
*When No. 846 infected, Exposure is 5.0 in day 4 at move 0
No. 6 exposure increased to 4.0 in day 4 at 1
No. 69 exposure increased to 1.0 in day 4 at 1
*When No. 92 infected, Exposure is 6.0 in day 4 at move 1
No. 107 exposure increased to 3.0 in day 4 at 1
No. 142 exposure increased to 4.0 in day 4 at 1
No. 144 exposure increased to 3.0 in day 4 at 1
No. 159 exposure increased to 2.0 in day 4 at 1
No. 225 exposure increased to 1.0 in day 4 at 1
No. 348 exposure increased to 2.0 in day 4 at 1
No. 371 exposure increased to 2.0 in day 4 at 1
No. 416 exposure increased to 2.0 in day 4 at 1
*When No. 432 infected, Exposure is 3.0 in day 4 at move 1
No. 440 exposure increased to 3.0 in day 4 at 1
No. 576 exposure increased to 2.0 in day 4 at 1
*When No. 726 infected, Exposure is 4.0 in day 4 at move 1
No. 744 exposure increased to 3.0 in day 4 at 1
No. 747 exposure increased to 5.0 in day 4 at 1
No. 748 exposure increased to 1.0 in day 4 at 1
No. 810 exposure increased to 3.0 in day 4 at 1
No. 812 exposure increased to 4.0 in day 4 at 1
*When No. 829 infected, Exposure is 2.0 in day 4 at move 1
No. 844 exposure increased to 2.0 in day 4 at 1
No. 914 exposure increased to 2.0 in day 4 at 1
*When No. 946 infected, Exposure is 6.0 in day 4 at move 1
*When No. 960 infected, Exposure is 3.0 in day 4 at move 1
No. 971 exposure increased to 3.0 in day 4 at 1
No. 985 exposure increased to 6.0 in day 4 at 1
   15/10000 [..............................] - ETA: 26:50:52 - reward: 899.4767*When No. 144 infected, Exposure is 3.0 in day 4 at move 0
*When No. 159 infected, Exposure is 2.0 in day 4 at move 0
*When No. 416 infected, Exposure is 2.0 in day 4 at move 0
*When No. 744 infected, Exposure is 3.0 in day 4 at move 0
*When No. 747 infected, Exposure is 5.0 in day 4 at move 0
*When No. 844 infected, Exposure is 2.0 in day 4 at move 0
*When No. 440 infected, Exposure is 3.0 in day 4 at move 1
*When No. 810 infected, Exposure is 3.0 in day 4 at move 1
*When No. 985 infected, Exposure is 6.0 in day 4 at move 2
*When No. 348 infected, Exposure is 2.0 in day 4 at move 4
*When No. 812 infected, Exposure is 4.0 in day 4 at move 4
No. 6 exposure increased to 5.0 in day 4 at 5
No. 69 exposure increased to 2.0 in day 4 at 5
No. 77 exposure increased to 1.0 in day 4 at 5
No. 107 exposure increased to 4.0 in day 4 at 5
No. 113 exposure increased to 1.0 in day 4 at 5
No. 142 exposure increased to 5.0 in day 4 at 5
No. 160 exposure increased to 1.0 in day 4 at 5
No. 171 exposure increased to 1.0 in day 4 at 5
No. 172 exposure increased to 2.0 in day 4 at 5
No. 225 exposure increased to 2.0 in day 4 at 5
No. 247 exposure increased to 1.0 in day 4 at 5
No. 282 exposure increased to 1.0 in day 4 at 5
No. 286 exposure increased to 1.0 in day 4 at 5
No. 313 exposure increased to 1.0 in day 4 at 5
No. 356 exposure increased to 1.0 in day 4 at 5
No. 371 exposure increased to 3.0 in day 4 at 5
No. 413 exposure increased to 2.0 in day 4 at 5
*When No. 576 infected, Exposure is 2.0 in day 4 at move 5
No. 622 exposure increased to 1.0 in day 4 at 5
No. 625 exposure increased to 1.0 in day 4 at 5
No. 748 exposure increased to 2.0 in day 4 at 5
No. 753 exposure increased to 1.0 in day 4 at 5
No. 775 exposure increased to 1.0 in day 4 at 5
No. 783 exposure increased to 1.0 in day 4 at 5
No. 792 exposure increased to 1.0 in day 4 at 5
No. 793 exposure increased to 1.0 in day 4 at 5
No. 808 exposure increased to 1.0 in day 4 at 5
No. 813 exposure increased to 1.0 in day 4 at 5
No. 864 exposure increased to 2.0 in day 4 at 5
No. 871 exposure increased to 1.0 in day 4 at 5
No. 900 exposure increased to 1.0 in day 4 at 5
No. 914 exposure increased to 3.0 in day 4 at 5
No. 971 exposure increased to 4.0 in day 4 at 5
No. 980 exposure increased to 1.0 in day 4 at 5
No. 988 exposure increased to 1.0 in day 4 at 5
No. 995 exposure increased to 1.0 in day 4 at 5
   16/10000 [..............................] - ETA: 28:01:56 - reward: 891.6906*When No. 6 infected, Exposure is 5.0 in day 4 at move 0
*When No. 142 infected, Exposure is 5.0 in day 4 at move 0
*When No. 69 infected, Exposure is 2.0 in day 4 at move 1
No. 77 exposure increased to 2.0 in day 4 at 1
No. 107 exposure increased to 5.0 in day 4 at 1
No. 108 exposure increased to 1.0 in day 4 at 1
No. 113 exposure increased to 2.0 in day 4 at 1
No. 160 exposure increased to 2.0 in day 4 at 1
No. 171 exposure increased to 2.0 in day 4 at 1
No. 172 exposure increased to 3.0 in day 4 at 1
*When No. 225 infected, Exposure is 2.0 in day 4 at move 1
No. 247 exposure increased to 2.0 in day 4 at 1
No. 282 exposure increased to 2.0 in day 4 at 1
No. 286 exposure increased to 2.0 in day 4 at 1
No. 313 exposure increased to 2.0 in day 4 at 1
No. 356 exposure increased to 2.0 in day 4 at 1
No. 371 exposure increased to 4.0 in day 4 at 1
No. 398 exposure increased to 2.0 in day 4 at 1
No. 403 exposure increased to 2.0 in day 4 at 1
No. 413 exposure increased to 3.0 in day 4 at 1
No. 486 exposure increased to 1.0 in day 4 at 1
No. 555 exposure increased to 1.0 in day 4 at 1
No. 593 exposure increased to 2.0 in day 4 at 1
No. 596 exposure increased to 2.0 in day 4 at 1
No. 622 exposure increased to 2.0 in day 4 at 1
No. 625 exposure increased to 2.0 in day 4 at 1
No. 693 exposure increased to 1.0 in day 4 at 1
No. 748 exposure increased to 3.0 in day 4 at 1
No. 753 exposure increased to 2.0 in day 4 at 1
No. 775 exposure increased to 2.0 in day 4 at 1
No. 783 exposure increased to 2.0 in day 4 at 1
No. 792 exposure increased to 2.0 in day 4 at 1
No. 793 exposure increased to 2.0 in day 4 at 1
No. 794 exposure increased to 1.0 in day 4 at 1
No. 808 exposure increased to 2.0 in day 4 at 1
No. 813 exposure increased to 2.0 in day 4 at 1
*When No. 864 infected, Exposure is 2.0 in day 4 at move 1
No. 871 exposure increased to 2.0 in day 4 at 1
No. 878 exposure increased to 1.0 in day 4 at 1
No. 900 exposure increased to 2.0 in day 4 at 1
No. 914 exposure increased to 4.0 in day 4 at 1
No. 941 exposure increased to 1.0 in day 4 at 1
*When No. 971 infected, Exposure is 4.0 in day 4 at move 1
No. 980 exposure increased to 2.0 in day 4 at 1
No. 987 exposure increased to 1.0 in day 4 at 1
No. 988 exposure increased to 2.0 in day 4 at 1
No. 995 exposure increased to 2.0 in day 4 at 1
   17/10000 [..............................] - ETA: 27:21:24 - reward: 890.6071*When No. 398 infected, Exposure is 2.0 in day 4 at move 0
No. 50 exposure increased to 2.0 in day 4 at 1
No. 77 exposure increased to 3.0 in day 4 at 1
No. 88 exposure increased to 2.0 in day 4 at 1
No. 100 exposure increased to 2.0 in day 4 at 1
No. 107 exposure increased to 6.0 in day 4 at 1
No. 108 exposure increased to 2.0 in day 4 at 1
No. 113 exposure increased to 3.0 in day 4 at 1
No. 118 exposure increased to 1.0 in day 4 at 1
No. 131 exposure increased to 2.0 in day 4 at 1
No. 145 exposure increased to 1.0 in day 4 at 1
No. 160 exposure increased to 3.0 in day 4 at 1
No. 171 exposure increased to 3.0 in day 4 at 1
No. 172 exposure increased to 4.0 in day 4 at 1
No. 218 exposure increased to 2.0 in day 4 at 1
No. 247 exposure increased to 3.0 in day 4 at 1
No. 282 exposure increased to 3.0 in day 4 at 1
No. 286 exposure increased to 3.0 in day 4 at 1
No. 304 exposure increased to 1.0 in day 4 at 1
No. 313 exposure increased to 3.0 in day 4 at 1
No. 356 exposure increased to 3.0 in day 4 at 1
No. 371 exposure increased to 5.0 in day 4 at 1
No. 403 exposure increased to 3.0 in day 4 at 1
No. 413 exposure increased to 4.0 in day 4 at 1
No. 449 exposure increased to 2.0 in day 4 at 1
No. 486 exposure increased to 2.0 in day 4 at 1
No. 491 exposure increased to 2.0 in day 4 at 1
No. 523 exposure increased to 1.0 in day 4 at 1
No. 528 exposure increased to 2.0 in day 4 at 1
No. 555 exposure increased to 2.0 in day 4 at 1
No. 574 exposure increased to 2.0 in day 4 at 1
No. 593 exposure increased to 3.0 in day 4 at 1
No. 596 exposure increased to 3.0 in day 4 at 1
No. 622 exposure increased to 3.0 in day 4 at 1
No. 625 exposure increased to 3.0 in day 4 at 1
No. 626 exposure increased to 2.0 in day 4 at 1
No. 657 exposure increased to 1.0 in day 4 at 1
No. 693 exposure increased to 2.0 in day 4 at 1
No. 695 exposure increased to 2.0 in day 4 at 1
*When No. 748 infected, Exposure is 3.0 in day 4 at move 1
No. 753 exposure increased to 3.0 in day 4 at 1
No. 775 exposure increased to 3.0 in day 4 at 1
No. 783 exposure increased to 3.0 in day 4 at 1
No. 792 exposure increased to 3.0 in day 4 at 1
No. 793 exposure increased to 3.0 in day 4 at 1
No. 794 exposure increased to 2.0 in day 4 at 1
No. 808 exposure increased to 3.0 in day 4 at 1
No. 813 exposure increased to 3.0 in day 4 at 1
No. 871 exposure increased to 3.0 in day 4 at 1
No. 876 exposure increased to 1.0 in day 4 at 1
No. 878 exposure increased to 2.0 in day 4 at 1
No. 900 exposure increased to 3.0 in day 4 at 1
*When No. 914 infected, Exposure is 4.0 in day 4 at move 1
No. 941 exposure increased to 2.0 in day 4 at 1
No. 980 exposure increased to 3.0 in day 4 at 1
No. 983 exposure increased to 2.0 in day 4 at 1
No. 987 exposure increased to 2.0 in day 4 at 1
No. 988 exposure increased to 3.0 in day 4 at 1
No. 995 exposure increased to 3.0 in day 4 at 1
   18/10000 [..............................] - ETA: 27:26:52 - reward: 884.8089*When No. 107 infected, Exposure is 6.0 in day 4 at move 0
*When No. 171 infected, Exposure is 3.0 in day 4 at move 0
*When No. 356 infected, Exposure is 3.0 in day 4 at move 0
*When No. 413 infected, Exposure is 4.0 in day 4 at move 0
*When No. 449 infected, Exposure is 2.0 in day 4 at move 0
*When No. 693 infected, Exposure is 2.0 in day 4 at move 0
*When No. 753 infected, Exposure is 3.0 in day 4 at move 0
*When No. 813 infected, Exposure is 3.0 in day 4 at move 0
*When No. 108 infected, Exposure is 2.0 in day 4 at move 1
*When No. 113 infected, Exposure is 3.0 in day 4 at move 1
*When No. 218 infected, Exposure is 2.0 in day 4 at move 1
*When No. 313 infected, Exposure is 3.0 in day 4 at move 1
*When No. 593 infected, Exposure is 3.0 in day 4 at move 1
*When No. 622 infected, Exposure is 3.0 in day 4 at move 1
*When No. 626 infected, Exposure is 2.0 in day 4 at move 1
*When No. 695 infected, Exposure is 2.0 in day 4 at move 1
*When No. 808 infected, Exposure is 3.0 in day 4 at move 1
*When No. 878 infected, Exposure is 2.0 in day 4 at move 1
*When No. 988 infected, Exposure is 3.0 in day 4 at move 1
*When No. 100 infected, Exposure is 2.0 in day 4 at move 2
*When No. 160 infected, Exposure is 3.0 in day 4 at move 2
*When No. 783 infected, Exposure is 3.0 in day 4 at move 2
*When No. 900 infected, Exposure is 3.0 in day 4 at move 2
*When No. 50 infected, Exposure is 2.0 in day 4 at move 3
*When No. 172 infected, Exposure is 4.0 in day 4 at move 3
*When No. 247 infected, Exposure is 3.0 in day 4 at move 3
*When No. 596 infected, Exposure is 3.0 in day 4 at move 3
*When No. 775 infected, Exposure is 3.0 in day 4 at move 3
*When No. 980 infected, Exposure is 3.0 in day 4 at move 3
*When No. 88 infected, Exposure is 2.0 in day 4 at move 4
*When No. 871 infected, Exposure is 3.0 in day 4 at move 4
No. 13 exposure increased to 1.0 in day 4 at 5
No. 16 exposure increased to 2.0 in day 4 at 5
No. 67 exposure increased to 1.0 in day 4 at 5
No. 77 exposure increased to 4.0 in day 4 at 5
No. 85 exposure increased to 1.0 in day 4 at 5
No. 102 exposure increased to 1.0 in day 4 at 5
No. 118 exposure increased to 2.0 in day 4 at 5
No. 131 exposure increased to 3.0 in day 4 at 5
No. 145 exposure increased to 2.0 in day 4 at 5
No. 163 exposure increased to 1.0 in day 4 at 5
No. 170 exposure increased to 1.0 in day 4 at 5
No. 194 exposure increased to 2.0 in day 4 at 5
No. 212 exposure increased to 1.0 in day 4 at 5
No. 215 exposure increased to 1.0 in day 4 at 5
No. 216 exposure increased to 2.0 in day 4 at 5
No. 243 exposure increased to 1.0 in day 4 at 5
No. 251 exposure increased to 1.0 in day 4 at 5
No. 255 exposure increased to 2.0 in day 4 at 5
No. 282 exposure increased to 4.0 in day 4 at 5
No. 286 exposure increased to 4.0 in day 4 at 5
No. 289 exposure increased to 1.0 in day 4 at 5
No. 304 exposure increased to 2.0 in day 4 at 5
No. 342 exposure increased to 1.0 in day 4 at 5
No. 371 exposure increased to 6.0 in day 4 at 5
No. 372 exposure increased to 2.0 in day 4 at 5
No. 403 exposure increased to 4.0 in day 4 at 5
No. 426 exposure increased to 2.0 in day 4 at 5
No. 486 exposure increased to 3.0 in day 4 at 5
No. 487 exposure increased to 1.0 in day 4 at 5
No. 491 exposure increased to 3.0 in day 4 at 5
No. 498 exposure increased to 1.0 in day 4 at 5
No. 500 exposure increased to 2.0 in day 4 at 5
No. 501 exposure increased to 1.0 in day 4 at 5
No. 523 exposure increased to 2.0 in day 4 at 5
No. 528 exposure increased to 3.0 in day 4 at 5
No. 547 exposure increased to 1.0 in day 4 at 5
No. 555 exposure increased to 3.0 in day 4 at 5
No. 574 exposure increased to 3.0 in day 4 at 5
No. 591 exposure increased to 1.0 in day 4 at 5
No. 625 exposure increased to 4.0 in day 4 at 5
No. 637 exposure increased to 1.0 in day 4 at 5
No. 651 exposure increased to 1.0 in day 4 at 5
No. 657 exposure increased to 2.0 in day 4 at 5
No. 660 exposure increased to 1.0 in day 4 at 5
No. 666 exposure increased to 1.0 in day 4 at 5
No. 670 exposure increased to 1.0 in day 4 at 5
No. 674 exposure increased to 1.0 in day 4 at 5
No. 751 exposure increased to 1.0 in day 4 at 5
No. 787 exposure increased to 1.0 in day 4 at 5
No. 792 exposure increased to 4.0 in day 4 at 5
No. 793 exposure increased to 4.0 in day 4 at 5
No. 794 exposure increased to 3.0 in day 4 at 5
No. 876 exposure increased to 2.0 in day 4 at 5
No. 881 exposure increased to 1.0 in day 4 at 5
No. 892 exposure increased to 1.0 in day 4 at 5
No. 906 exposure increased to 1.0 in day 4 at 5
No. 915 exposure increased to 1.0 in day 4 at 5
No. 924 exposure increased to 1.0 in day 4 at 5
*When No. 941 infected, Exposure is 2.0 in day 4 at move 5
No. 942 exposure increased to 1.0 in day 4 at 5
No. 968 exposure increased to 1.0 in day 4 at 5
No. 976 exposure increased to 1.0 in day 4 at 5
No. 977 exposure increased to 1.0 in day 4 at 5
No. 983 exposure increased to 3.0 in day 4 at 5
No. 987 exposure increased to 3.0 in day 4 at 5
No. 995 exposure increased to 4.0 in day 4 at 5
   19/10000 [..............................] - ETA: 29:34:02 - reward: 878.2063*When No. 145 infected, Exposure is 2.0 in day 4 at move 0
*When No. 282 infected, Exposure is 4.0 in day 4 at move 0
*When No. 491 infected, Exposure is 3.0 in day 4 at move 0
*When No. 625 infected, Exposure is 4.0 in day 4 at move 0
*When No. 794 infected, Exposure is 3.0 in day 4 at move 0
*When No. 987 infected, Exposure is 3.0 in day 4 at move 0
*When No. 371 infected, Exposure is 6.0 in day 4 at move 1
*When No. 792 infected, Exposure is 4.0 in day 4 at move 1
*When No. 16 infected, Exposure is 2.0 in day 4 at move 2
*When No. 216 infected, Exposure is 2.0 in day 4 at move 2
*When No. 995 infected, Exposure is 4.0 in day 4 at move 2
*When No. 77 infected, Exposure is 4.0 in day 4 at move 3
*When No. 131 infected, Exposure is 3.0 in day 4 at move 3
*When No. 255 infected, Exposure is 2.0 in day 4 at move 3
*When No. 286 infected, Exposure is 4.0 in day 4 at move 3
*When No. 426 infected, Exposure is 2.0 in day 4 at move 3
*When No. 574 infected, Exposure is 3.0 in day 4 at move 3
*When No. 486 infected, Exposure is 3.0 in day 4 at move 4
No. 12 exposure increased to 1.0 in day 4 at 5
No. 13 exposure increased to 2.0 in day 4 at 5
No. 22 exposure increased to 1.0 in day 4 at 5
No. 25 exposure increased to 1.0 in day 4 at 5
No. 51 exposure increased to 1.0 in day 4 at 5
No. 57 exposure increased to 1.0 in day 4 at 5
No. 67 exposure increased to 2.0 in day 4 at 5
No. 82 exposure increased to 1.0 in day 4 at 5
No. 85 exposure increased to 2.0 in day 4 at 5
No. 102 exposure increased to 2.0 in day 4 at 5
No. 118 exposure increased to 3.0 in day 4 at 5
No. 123 exposure increased to 2.0 in day 4 at 5
No. 127 exposure increased to 1.0 in day 4 at 5
No. 163 exposure increased to 2.0 in day 4 at 5
No. 170 exposure increased to 2.0 in day 4 at 5
No. 182 exposure increased to 1.0 in day 4 at 5
No. 194 exposure increased to 3.0 in day 4 at 5
No. 205 exposure increased to 1.0 in day 4 at 5
No. 208 exposure increased to 2.0 in day 4 at 5
No. 211 exposure increased to 1.0 in day 4 at 5
No. 212 exposure increased to 2.0 in day 4 at 5
No. 215 exposure increased to 2.0 in day 4 at 5
No. 229 exposure increased to 1.0 in day 4 at 5
No. 231 exposure increased to 1.0 in day 4 at 5
No. 243 exposure increased to 2.0 in day 4 at 5
No. 249 exposure increased to 1.0 in day 4 at 5
No. 251 exposure increased to 2.0 in day 4 at 5
No. 254 exposure increased to 1.0 in day 4 at 5
No. 257 exposure increased to 2.0 in day 4 at 5
No. 275 exposure increased to 1.0 in day 4 at 5
No. 289 exposure increased to 2.0 in day 4 at 5
No. 304 exposure increased to 3.0 in day 4 at 5
No. 308 exposure increased to 2.0 in day 4 at 5
No. 309 exposure increased to 1.0 in day 4 at 5
No. 314 exposure increased to 1.0 in day 4 at 5
No. 319 exposure increased to 1.0 in day 4 at 5
No. 333 exposure increased to 1.0 in day 4 at 5
No. 337 exposure increased to 1.0 in day 4 at 5
No. 342 exposure increased to 2.0 in day 4 at 5
No. 360 exposure increased to 1.0 in day 4 at 5
No. 372 exposure increased to 3.0 in day 4 at 5
No. 375 exposure increased to 2.0 in day 4 at 5
No. 382 exposure increased to 1.0 in day 4 at 5
No. 401 exposure increased to 1.0 in day 4 at 5
No. 403 exposure increased to 5.0 in day 4 at 5
No. 409 exposure increased to 1.0 in day 4 at 5
No. 424 exposure increased to 1.0 in day 4 at 5
No. 438 exposure increased to 1.0 in day 4 at 5
No. 454 exposure increased to 1.0 in day 4 at 5
No. 456 exposure increased to 1.0 in day 4 at 5
No. 475 exposure increased to 2.0 in day 4 at 5
No. 487 exposure increased to 2.0 in day 4 at 5
No. 488 exposure increased to 1.0 in day 4 at 5
No. 498 exposure increased to 2.0 in day 4 at 5
No. 500 exposure increased to 3.0 in day 4 at 5
No. 501 exposure increased to 2.0 in day 4 at 5
No. 510 exposure increased to 2.0 in day 4 at 5
No. 511 exposure increased to 1.0 in day 4 at 5
No. 523 exposure increased to 3.0 in day 4 at 5
No. 525 exposure increased to 1.0 in day 4 at 5
No. 528 exposure increased to 4.0 in day 4 at 5
No. 547 exposure increased to 2.0 in day 4 at 5
No. 549 exposure increased to 1.0 in day 4 at 5
No. 555 exposure increased to 4.0 in day 4 at 5
No. 578 exposure increased to 1.0 in day 4 at 5
No. 591 exposure increased to 2.0 in day 4 at 5
No. 597 exposure increased to 1.0 in day 4 at 5
No. 609 exposure increased to 1.0 in day 4 at 5
No. 613 exposure increased to 1.0 in day 4 at 5
No. 637 exposure increased to 2.0 in day 4 at 5
No. 651 exposure increased to 2.0 in day 4 at 5
No. 657 exposure increased to 3.0 in day 4 at 5
No. 660 exposure increased to 2.0 in day 4 at 5
No. 664 exposure increased to 1.0 in day 4 at 5
No. 666 exposure increased to 2.0 in day 4 at 5
No. 670 exposure increased to 2.0 in day 4 at 5
No. 674 exposure increased to 2.0 in day 4 at 5
No. 679 exposure increased to 1.0 in day 4 at 5
No. 689 exposure increased to 1.0 in day 4 at 5
No. 713 exposure increased to 1.0 in day 4 at 5
No. 718 exposure increased to 1.0 in day 4 at 5
No. 733 exposure increased to 1.0 in day 4 at 5
No. 741 exposure increased to 1.0 in day 4 at 5
No. 745 exposure increased to 1.0 in day 4 at 5
No. 751 exposure increased to 2.0 in day 4 at 5
No. 754 exposure increased to 1.0 in day 4 at 5
No. 761 exposure increased to 2.0 in day 4 at 5
No. 770 exposure increased to 1.0 in day 4 at 5
No. 787 exposure increased to 2.0 in day 4 at 5
No. 793 exposure increased to 5.0 in day 4 at 5
No. 876 exposure increased to 3.0 in day 4 at 5
No. 880 exposure increased to 1.0 in day 4 at 5
No. 881 exposure increased to 2.0 in day 4 at 5
No. 892 exposure increased to 2.0 in day 4 at 5
No. 903 exposure increased to 1.0 in day 4 at 5
No. 906 exposure increased to 2.0 in day 4 at 5
No. 913 exposure increased to 1.0 in day 4 at 5
No. 915 exposure increased to 2.0 in day 4 at 5
No. 924 exposure increased to 2.0 in day 4 at 5
No. 936 exposure increased to 2.0 in day 4 at 5
No. 942 exposure increased to 2.0 in day 4 at 5
No. 968 exposure increased to 2.0 in day 4 at 5
No. 972 exposure increased to 1.0 in day 4 at 5
No. 974 exposure increased to 1.0 in day 4 at 5
No. 976 exposure increased to 2.0 in day 4 at 5
No. 977 exposure increased to 2.0 in day 4 at 5
*When No. 983 infected, Exposure is 3.0 in day 4 at move 5
   20/10000 [..............................] - ETA: 30:28:08 - reward: 875.8910*When No. 251 infected, Exposure is 2.0 in day 4 at move 0
*When No. 257 infected, Exposure is 2.0 in day 4 at move 0
*When No. 500 infected, Exposure is 3.0 in day 4 at move 0
*When No. 501 infected, Exposure is 2.0 in day 4 at move 0
*When No. 528 infected, Exposure is 4.0 in day 4 at move 0
*When No. 555 infected, Exposure is 4.0 in day 4 at move 0
*When No. 670 infected, Exposure is 2.0 in day 4 at move 0
*When No. 793 infected, Exposure is 5.0 in day 4 at move 0
*When No. 212 infected, Exposure is 2.0 in day 4 at move 1
*When No. 243 infected, Exposure is 2.0 in day 4 at move 1
*When No. 403 infected, Exposure is 5.0 in day 4 at move 1
*When No. 651 infected, Exposure is 2.0 in day 4 at move 1
*When No. 906 infected, Exposure is 2.0 in day 4 at move 1
*When No. 123 infected, Exposure is 2.0 in day 4 at move 2
*When No. 523 infected, Exposure is 3.0 in day 4 at move 2
*When No. 194 infected, Exposure is 3.0 in day 4 at move 3
*When No. 475 infected, Exposure is 2.0 in day 4 at move 3
*When No. 751 infected, Exposure is 2.0 in day 4 at move 3
*When No. 85 infected, Exposure is 2.0 in day 4 at move 4
*When No. 118 infected, Exposure is 3.0 in day 4 at move 4
*When No. 170 infected, Exposure is 2.0 in day 4 at move 4
*When No. 208 infected, Exposure is 2.0 in day 4 at move 4
*When No. 342 infected, Exposure is 2.0 in day 4 at move 4
*When No. 547 infected, Exposure is 2.0 in day 4 at move 4
*When No. 876 infected, Exposure is 3.0 in day 4 at move 4
*When No. 968 infected, Exposure is 2.0 in day 4 at move 4
No. 5 exposure increased to 1.0 in day 4 at 5
No. 12 exposure increased to 2.0 in day 4 at 5
No. 13 exposure increased to 3.0 in day 4 at 5
No. 22 exposure increased to 2.0 in day 4 at 5
No. 25 exposure increased to 2.0 in day 4 at 5
No. 51 exposure increased to 2.0 in day 4 at 5
No. 54 exposure increased to 2.0 in day 4 at 5
No. 57 exposure increased to 2.0 in day 4 at 5
No. 62 exposure increased to 1.0 in day 4 at 5
No. 67 exposure increased to 3.0 in day 4 at 5
No. 80 exposure increased to 1.0 in day 4 at 5
No. 82 exposure increased to 2.0 in day 4 at 5
No. 90 exposure increased to 1.0 in day 4 at 5
*When No. 102 infected, Exposure is 2.0 in day 4 at move 5
No. 127 exposure increased to 2.0 in day 4 at 5
No. 136 exposure increased to 1.0 in day 4 at 5
*When No. 163 infected, Exposure is 2.0 in day 4 at move 5
No. 164 exposure increased to 1.0 in day 4 at 5
No. 182 exposure increased to 2.0 in day 4 at 5
No. 189 exposure increased to 1.0 in day 4 at 5
No. 195 exposure increased to 1.0 in day 4 at 5
No. 205 exposure increased to 2.0 in day 4 at 5
No. 211 exposure increased to 2.0 in day 4 at 5
No. 215 exposure increased to 3.0 in day 4 at 5
No. 229 exposure increased to 2.0 in day 4 at 5
No. 231 exposure increased to 2.0 in day 4 at 5
No. 249 exposure increased to 2.0 in day 4 at 5
No. 254 exposure increased to 2.0 in day 4 at 5
No. 258 exposure increased to 1.0 in day 4 at 5
No. 275 exposure increased to 2.0 in day 4 at 5
No. 283 exposure increased to 1.0 in day 4 at 5
*When No. 289 infected, Exposure is 2.0 in day 4 at move 5
No. 304 exposure increased to 4.0 in day 4 at 5
No. 308 exposure increased to 3.0 in day 4 at 5
No. 309 exposure increased to 2.0 in day 4 at 5
No. 314 exposure increased to 2.0 in day 4 at 5
No. 319 exposure increased to 2.0 in day 4 at 5
No. 333 exposure increased to 2.0 in day 4 at 5
No. 337 exposure increased to 2.0 in day 4 at 5
No. 360 exposure increased to 2.0 in day 4 at 5
No. 365 exposure increased to 1.0 in day 4 at 5
No. 370 exposure increased to 1.0 in day 4 at 5
No. 372 exposure increased to 4.0 in day 4 at 5
No. 375 exposure increased to 3.0 in day 4 at 5
No. 382 exposure increased to 2.0 in day 4 at 5
No. 401 exposure increased to 2.0 in day 4 at 5
No. 409 exposure increased to 2.0 in day 4 at 5
No. 424 exposure increased to 2.0 in day 4 at 5
No. 438 exposure increased to 2.0 in day 4 at 5
No. 454 exposure increased to 2.0 in day 4 at 5
No. 455 exposure increased to 1.0 in day 4 at 5
No. 456 exposure increased to 2.0 in day 4 at 5
No. 487 exposure increased to 3.0 in day 4 at 5
No. 488 exposure increased to 2.0 in day 4 at 5
No. 498 exposure increased to 3.0 in day 4 at 5
No. 503 exposure increased to 1.0 in day 4 at 5
No. 504 exposure increased to 1.0 in day 4 at 5
No. 510 exposure increased to 3.0 in day 4 at 5
No. 511 exposure increased to 2.0 in day 4 at 5
No. 524 exposure increased to 1.0 in day 4 at 5
No. 525 exposure increased to 2.0 in day 4 at 5
No. 549 exposure increased to 2.0 in day 4 at 5
No. 571 exposure increased to 1.0 in day 4 at 5
No. 578 exposure increased to 2.0 in day 4 at 5
No. 582 exposure increased to 1.0 in day 4 at 5
No. 591 exposure increased to 3.0 in day 4 at 5
No. 597 exposure increased to 2.0 in day 4 at 5
No. 609 exposure increased to 2.0 in day 4 at 5
No. 613 exposure increased to 2.0 in day 4 at 5
No. 637 exposure increased to 3.0 in day 4 at 5
No. 648 exposure increased to 2.0 in day 4 at 5
No. 657 exposure increased to 4.0 in day 4 at 5
No. 660 exposure increased to 3.0 in day 4 at 5
No. 664 exposure increased to 2.0 in day 4 at 5
No. 666 exposure increased to 3.0 in day 4 at 5
No. 671 exposure increased to 1.0 in day 4 at 5
No. 674 exposure increased to 3.0 in day 4 at 5
No. 679 exposure increased to 2.0 in day 4 at 5
No. 689 exposure increased to 2.0 in day 4 at 5
No. 713 exposure increased to 2.0 in day 4 at 5
No. 718 exposure increased to 2.0 in day 4 at 5
No. 733 exposure increased to 2.0 in day 4 at 5
No. 734 exposure increased to 1.0 in day 4 at 5
No. 741 exposure increased to 2.0 in day 4 at 5
No. 745 exposure increased to 2.0 in day 4 at 5
No. 754 exposure increased to 2.0 in day 4 at 5
No. 755 exposure increased to 1.0 in day 4 at 5
No. 761 exposure increased to 3.0 in day 4 at 5
No. 770 exposure increased to 2.0 in day 4 at 5
No. 787 exposure increased to 3.0 in day 4 at 5
No. 791 exposure increased to 2.0 in day 4 at 5
No. 799 exposure increased to 1.0 in day 4 at 5
No. 811 exposure increased to 1.0 in day 4 at 5
No. 822 exposure increased to 1.0 in day 4 at 5
No. 835 exposure increased to 1.0 in day 4 at 5
No. 848 exposure increased to 1.0 in day 4 at 5
No. 850 exposure increased to 1.0 in day 4 at 5
No. 879 exposure increased to 1.0 in day 4 at 5
No. 880 exposure increased to 2.0 in day 4 at 5
No. 881 exposure increased to 3.0 in day 4 at 5
No. 892 exposure increased to 3.0 in day 4 at 5
No. 903 exposure increased to 2.0 in day 4 at 5
No. 913 exposure increased to 2.0 in day 4 at 5
No. 915 exposure increased to 3.0 in day 4 at 5
No. 919 exposure increased to 1.0 in day 4 at 5
No. 923 exposure increased to 1.0 in day 4 at 5
No. 924 exposure increased to 3.0 in day 4 at 5
No. 927 exposure increased to 1.0 in day 4 at 5
No. 936 exposure increased to 3.0 in day 4 at 5
No. 942 exposure increased to 3.0 in day 4 at 5
No. 952 exposure increased to 1.0 in day 4 at 5
No. 972 exposure increased to 2.0 in day 4 at 5
No. 974 exposure increased to 2.0 in day 4 at 5
No. 976 exposure increased to 3.0 in day 4 at 5
No. 977 exposure increased to 3.0 in day 4 at 5
No. 981 exposure increased to 1.0 in day 4 at 5
   21/10000 [..............................] - ETA: 31:11:20 - reward: 869.2781*When No. 12 infected, Exposure is 2.0 in day 4 at move 0
*When No. 22 infected, Exposure is 2.0 in day 4 at move 0
*When No. 215 infected, Exposure is 3.0 in day 4 at move 0
*When No. 375 infected, Exposure is 3.0 in day 4 at move 0
*When No. 498 infected, Exposure is 3.0 in day 4 at move 0
*When No. 578 infected, Exposure is 2.0 in day 4 at move 0
*When No. 613 infected, Exposure is 2.0 in day 4 at move 0
*When No. 689 infected, Exposure is 2.0 in day 4 at move 0
*When No. 787 infected, Exposure is 3.0 in day 4 at move 0
*When No. 881 infected, Exposure is 3.0 in day 4 at move 0
*When No. 903 infected, Exposure is 2.0 in day 4 at move 0
*When No. 915 infected, Exposure is 3.0 in day 4 at move 0
*When No. 977 infected, Exposure is 3.0 in day 4 at move 0
*When No. 127 infected, Exposure is 2.0 in day 4 at move 1
*When No. 275 infected, Exposure is 2.0 in day 4 at move 1
*When No. 308 infected, Exposure is 3.0 in day 4 at move 1
*When No. 314 infected, Exposure is 2.0 in day 4 at move 1
*When No. 337 infected, Exposure is 2.0 in day 4 at move 1
*When No. 657 infected, Exposure is 4.0 in day 4 at move 1
*When No. 660 infected, Exposure is 3.0 in day 4 at move 1
*When No. 674 infected, Exposure is 3.0 in day 4 at move 1
*When No. 679 infected, Exposure is 2.0 in day 4 at move 1
*When No. 761 infected, Exposure is 3.0 in day 4 at move 1
*When No. 972 infected, Exposure is 2.0 in day 4 at move 1
*When No. 13 infected, Exposure is 3.0 in day 4 at move 2
*When No. 609 infected, Exposure is 2.0 in day 4 at move 2
*When No. 745 infected, Exposure is 2.0 in day 4 at move 2
*When No. 924 infected, Exposure is 3.0 in day 4 at move 2
*When No. 372 infected, Exposure is 4.0 in day 4 at move 3
*When No. 424 infected, Exposure is 2.0 in day 4 at move 3
*When No. 637 infected, Exposure is 3.0 in day 4 at move 3
*When No. 229 infected, Exposure is 2.0 in day 4 at move 4
*When No. 231 infected, Exposure is 2.0 in day 4 at move 4
*When No. 304 infected, Exposure is 4.0 in day 4 at move 4
*When No. 488 infected, Exposure is 2.0 in day 4 at move 4
*When No. 648 infected, Exposure is 2.0 in day 4 at move 4
*When No. 754 infected, Exposure is 2.0 in day 4 at move 4
*When No. 976 infected, Exposure is 3.0 in day 4 at move 4
No. 5 exposure increased to 2.0 in day 4 at 5
No. 14 exposure increased to 1.0 in day 4 at 5
No. 21 exposure increased to 1.0 in day 4 at 5
No. 25 exposure increased to 3.0 in day 4 at 5
No. 51 exposure increased to 3.0 in day 4 at 5
No. 54 exposure increased to 3.0 in day 4 at 5
No. 57 exposure increased to 3.0 in day 4 at 5
No. 62 exposure increased to 2.0 in day 4 at 5
No. 67 exposure increased to 4.0 in day 4 at 5
No. 80 exposure increased to 2.0 in day 4 at 5
No. 82 exposure increased to 3.0 in day 4 at 5
No. 90 exposure increased to 2.0 in day 4 at 5
No. 99 exposure increased to 1.0 in day 4 at 5
No. 126 exposure increased to 1.0 in day 4 at 5
No. 136 exposure increased to 2.0 in day 4 at 5
No. 140 exposure increased to 1.0 in day 4 at 5
No. 149 exposure increased to 1.0 in day 4 at 5
No. 152 exposure increased to 1.0 in day 4 at 5
No. 158 exposure increased to 1.0 in day 4 at 5
No. 164 exposure increased to 2.0 in day 4 at 5
No. 182 exposure increased to 3.0 in day 4 at 5
No. 186 exposure increased to 1.0 in day 4 at 5
No. 189 exposure increased to 2.0 in day 4 at 5
No. 190 exposure increased to 1.0 in day 4 at 5
No. 195 exposure increased to 2.0 in day 4 at 5
No. 205 exposure increased to 3.0 in day 4 at 5
No. 211 exposure increased to 3.0 in day 4 at 5
*When No. 249 infected, Exposure is 2.0 in day 4 at move 5
No. 254 exposure increased to 3.0 in day 4 at 5
No. 258 exposure increased to 2.0 in day 4 at 5
No. 263 exposure increased to 1.0 in day 4 at 5
No. 283 exposure increased to 2.0 in day 4 at 5
No. 300 exposure increased to 1.0 in day 4 at 5
No. 306 exposure increased to 1.0 in day 4 at 5
No. 309 exposure increased to 3.0 in day 4 at 5
No. 315 exposure increased to 1.0 in day 4 at 5
No. 319 exposure increased to 3.0 in day 4 at 5
No. 333 exposure increased to 3.0 in day 4 at 5
No. 360 exposure increased to 3.0 in day 4 at 5
No. 365 exposure increased to 2.0 in day 4 at 5
No. 370 exposure increased to 2.0 in day 4 at 5
No. 373 exposure increased to 1.0 in day 4 at 5
No. 382 exposure increased to 3.0 in day 4 at 5
No. 383 exposure increased to 1.0 in day 4 at 5
No. 392 exposure increased to 1.0 in day 4 at 5
No. 401 exposure increased to 3.0 in day 4 at 5
No. 409 exposure increased to 3.0 in day 4 at 5
No. 419 exposure increased to 1.0 in day 4 at 5
No. 423 exposure increased to 1.0 in day 4 at 5
No. 425 exposure increased to 1.0 in day 4 at 5
No. 429 exposure increased to 1.0 in day 4 at 5
No. 437 exposure increased to 1.0 in day 4 at 5
No. 438 exposure increased to 3.0 in day 4 at 5
No. 445 exposure increased to 1.0 in day 4 at 5
No. 454 exposure increased to 3.0 in day 4 at 5
No. 455 exposure increased to 2.0 in day 4 at 5
No. 456 exposure increased to 3.0 in day 4 at 5
No. 467 exposure increased to 1.0 in day 4 at 5
No. 478 exposure increased to 1.0 in day 4 at 5
No. 487 exposure increased to 4.0 in day 4 at 5
No. 494 exposure increased to 1.0 in day 4 at 5
No. 496 exposure increased to 1.0 in day 4 at 5
No. 503 exposure increased to 2.0 in day 4 at 5
No. 504 exposure increased to 2.0 in day 4 at 5
No. 509 exposure increased to 1.0 in day 4 at 5
No. 510 exposure increased to 4.0 in day 4 at 5
No. 511 exposure increased to 3.0 in day 4 at 5
No. 517 exposure increased to 1.0 in day 4 at 5
No. 524 exposure increased to 2.0 in day 4 at 5
No. 525 exposure increased to 3.0 in day 4 at 5
*When No. 549 infected, Exposure is 2.0 in day 4 at move 5
No. 553 exposure increased to 1.0 in day 4 at 5
No. 557 exposure increased to 1.0 in day 4 at 5
No. 562 exposure increased to 1.0 in day 4 at 5
No. 571 exposure increased to 2.0 in day 4 at 5
No. 579 exposure increased to 2.0 in day 4 at 5
No. 582 exposure increased to 2.0 in day 4 at 5
No. 589 exposure increased to 1.0 in day 4 at 5
No. 591 exposure increased to 4.0 in day 4 at 5
*When No. 597 infected, Exposure is 2.0 in day 4 at move 5
No. 629 exposure increased to 1.0 in day 4 at 5
No. 650 exposure increased to 1.0 in day 4 at 5
No. 659 exposure increased to 1.0 in day 4 at 5
No. 661 exposure increased to 1.0 in day 4 at 5
No. 664 exposure increased to 3.0 in day 4 at 5
No. 666 exposure increased to 4.0 in day 4 at 5
No. 671 exposure increased to 2.0 in day 4 at 5
No. 675 exposure increased to 1.0 in day 4 at 5
No. 698 exposure increased to 1.0 in day 4 at 5
No. 702 exposure increased to 1.0 in day 4 at 5
No. 713 exposure increased to 3.0 in day 4 at 5
No. 716 exposure increased to 1.0 in day 4 at 5
*When No. 718 infected, Exposure is 2.0 in day 4 at move 5
No. 732 exposure increased to 1.0 in day 4 at 5
*When No. 733 infected, Exposure is 2.0 in day 4 at move 5
No. 734 exposure increased to 2.0 in day 4 at 5
No. 741 exposure increased to 3.0 in day 4 at 5
No. 743 exposure increased to 2.0 in day 4 at 5
No. 755 exposure increased to 2.0 in day 4 at 5
No. 765 exposure increased to 1.0 in day 4 at 5
No. 770 exposure increased to 3.0 in day 4 at 5
No. 777 exposure increased to 1.0 in day 4 at 5
No. 791 exposure increased to 3.0 in day 4 at 5
No. 799 exposure increased to 2.0 in day 4 at 5
No. 811 exposure increased to 2.0 in day 4 at 5
No. 822 exposure increased to 2.0 in day 4 at 5
No. 835 exposure increased to 2.0 in day 4 at 5
No. 837 exposure increased to 1.0 in day 4 at 5
No. 848 exposure increased to 2.0 in day 4 at 5
No. 850 exposure increased to 2.0 in day 4 at 5
No. 879 exposure increased to 2.0 in day 4 at 5
No. 880 exposure increased to 3.0 in day 4 at 5
No. 892 exposure increased to 4.0 in day 4 at 5
No. 897 exposure increased to 1.0 in day 4 at 5
*When No. 913 infected, Exposure is 2.0 in day 4 at move 5
No. 918 exposure increased to 2.0 in day 4 at 5
No. 919 exposure increased to 2.0 in day 4 at 5
No. 923 exposure increased to 2.0 in day 4 at 5
No. 927 exposure increased to 2.0 in day 4 at 5
No. 936 exposure increased to 4.0 in day 4 at 5
No. 942 exposure increased to 4.0 in day 4 at 5
No. 944 exposure increased to 1.0 in day 4 at 5
No. 947 exposure increased to 1.0 in day 4 at 5
No. 952 exposure increased to 2.0 in day 4 at 5
*When No. 974 infected, Exposure is 2.0 in day 4 at move 5
No. 981 exposure increased to 2.0 in day 4 at 5
No. 991 exposure increased to 1.0 in day 4 at 5
   22/10000 [..............................] - ETA: 31:44:17 - reward: 862.2855*When No. 62 infected, Exposure is 2.0 in day 4 at move 0
*When No. 195 infected, Exposure is 2.0 in day 4 at move 0
*When No. 319 infected, Exposure is 3.0 in day 4 at move 0
*When No. 333 infected, Exposure is 3.0 in day 4 at move 0
*When No. 360 infected, Exposure is 3.0 in day 4 at move 0
*When No. 409 infected, Exposure is 3.0 in day 4 at move 0
*When No. 510 infected, Exposure is 4.0 in day 4 at move 0
*When No. 511 infected, Exposure is 3.0 in day 4 at move 0
*When No. 591 infected, Exposure is 4.0 in day 4 at move 0
*When No. 666 infected, Exposure is 4.0 in day 4 at move 0
*When No. 734 infected, Exposure is 2.0 in day 4 at move 0
*When No. 791 infected, Exposure is 3.0 in day 4 at move 0
*When No. 880 infected, Exposure is 3.0 in day 4 at move 0
*When No. 892 infected, Exposure is 4.0 in day 4 at move 0
*When No. 923 infected, Exposure is 2.0 in day 4 at move 0
No. 5 exposure increased to 3.0 in day 4 at 1
No. 14 exposure increased to 2.0 in day 4 at 1
No. 21 exposure increased to 2.0 in day 4 at 1
No. 25 exposure increased to 4.0 in day 4 at 1
No. 34 exposure increased to 1.0 in day 4 at 1
*When No. 51 infected, Exposure is 3.0 in day 4 at move 1
No. 54 exposure increased to 4.0 in day 4 at 1
*When No. 57 infected, Exposure is 3.0 in day 4 at move 1
No. 58 exposure increased to 1.0 in day 4 at 1
No. 67 exposure increased to 5.0 in day 4 at 1
No. 78 exposure increased to 1.0 in day 4 at 1
No. 80 exposure increased to 3.0 in day 4 at 1
*When No. 82 infected, Exposure is 3.0 in day 4 at move 1
No. 90 exposure increased to 3.0 in day 4 at 1
No. 99 exposure increased to 2.0 in day 4 at 1
No. 126 exposure increased to 2.0 in day 4 at 1
*When No. 136 infected, Exposure is 2.0 in day 4 at move 1
No. 140 exposure increased to 2.0 in day 4 at 1
No. 148 exposure increased to 2.0 in day 4 at 1
No. 149 exposure increased to 2.0 in day 4 at 1
No. 150 exposure increased to 2.0 in day 4 at 1
No. 152 exposure increased to 2.0 in day 4 at 1
No. 158 exposure increased to 2.0 in day 4 at 1
No. 164 exposure increased to 3.0 in day 4 at 1
No. 180 exposure increased to 1.0 in day 4 at 1
No. 182 exposure increased to 4.0 in day 4 at 1
No. 186 exposure increased to 2.0 in day 4 at 1
No. 189 exposure increased to 3.0 in day 4 at 1
No. 190 exposure increased to 2.0 in day 4 at 1
No. 205 exposure increased to 4.0 in day 4 at 1
No. 211 exposure increased to 4.0 in day 4 at 1
No. 254 exposure increased to 4.0 in day 4 at 1
No. 258 exposure increased to 3.0 in day 4 at 1
No. 262 exposure increased to 1.0 in day 4 at 1
No. 263 exposure increased to 2.0 in day 4 at 1
No. 283 exposure increased to 3.0 in day 4 at 1
No. 300 exposure increased to 2.0 in day 4 at 1
No. 306 exposure increased to 2.0 in day 4 at 1
*When No. 309 infected, Exposure is 3.0 in day 4 at move 1
No. 315 exposure increased to 2.0 in day 4 at 1
No. 349 exposure increased to 1.0 in day 4 at 1
No. 365 exposure increased to 3.0 in day 4 at 1
No. 370 exposure increased to 3.0 in day 4 at 1
No. 373 exposure increased to 2.0 in day 4 at 1
No. 377 exposure increased to 1.0 in day 4 at 1
No. 380 exposure increased to 1.0 in day 4 at 1
No. 382 exposure increased to 4.0 in day 4 at 1
No. 383 exposure increased to 2.0 in day 4 at 1
No. 392 exposure increased to 2.0 in day 4 at 1
No. 401 exposure increased to 4.0 in day 4 at 1
No. 419 exposure increased to 2.0 in day 4 at 1
No. 423 exposure increased to 2.0 in day 4 at 1
No. 425 exposure increased to 2.0 in day 4 at 1
No. 429 exposure increased to 2.0 in day 4 at 1
No. 430 exposure increased to 1.0 in day 4 at 1
No. 437 exposure increased to 2.0 in day 4 at 1
No. 438 exposure increased to 4.0 in day 4 at 1
No. 445 exposure increased to 2.0 in day 4 at 1
No. 453 exposure increased to 2.0 in day 4 at 1
No. 454 exposure increased to 4.0 in day 4 at 1
No. 455 exposure increased to 3.0 in day 4 at 1
No. 456 exposure increased to 4.0 in day 4 at 1
No. 467 exposure increased to 2.0 in day 4 at 1
No. 478 exposure increased to 2.0 in day 4 at 1
*When No. 487 infected, Exposure is 4.0 in day 4 at move 1
No. 490 exposure increased to 2.0 in day 4 at 1
No. 494 exposure increased to 2.0 in day 4 at 1
No. 496 exposure increased to 2.0 in day 4 at 1
No. 499 exposure increased to 1.0 in day 4 at 1
No. 503 exposure increased to 3.0 in day 4 at 1
*When No. 504 infected, Exposure is 2.0 in day 4 at move 1
No. 509 exposure increased to 2.0 in day 4 at 1
No. 517 exposure increased to 2.0 in day 4 at 1
No. 524 exposure increased to 3.0 in day 4 at 1
No. 525 exposure increased to 4.0 in day 4 at 1
No. 536 exposure increased to 2.0 in day 4 at 1
No. 553 exposure increased to 2.0 in day 4 at 1
No. 554 exposure increased to 1.0 in day 4 at 1
No. 557 exposure increased to 2.0 in day 4 at 1
No. 562 exposure increased to 2.0 in day 4 at 1
*When No. 571 infected, Exposure is 2.0 in day 4 at move 1
No. 579 exposure increased to 3.0 in day 4 at 1
No. 582 exposure increased to 3.0 in day 4 at 1
No. 589 exposure increased to 2.0 in day 4 at 1
No. 618 exposure increased to 1.0 in day 4 at 1
No. 629 exposure increased to 2.0 in day 4 at 1
No. 647 exposure increased to 1.0 in day 4 at 1
No. 650 exposure increased to 2.0 in day 4 at 1
No. 659 exposure increased to 2.0 in day 4 at 1
No. 661 exposure increased to 2.0 in day 4 at 1
No. 662 exposure increased to 2.0 in day 4 at 1
No. 664 exposure increased to 4.0 in day 4 at 1
*When No. 671 infected, Exposure is 2.0 in day 4 at move 1
No. 675 exposure increased to 2.0 in day 4 at 1
No. 698 exposure increased to 2.0 in day 4 at 1
No. 701 exposure increased to 2.0 in day 4 at 1
No. 702 exposure increased to 2.0 in day 4 at 1
*When No. 713 infected, Exposure is 3.0 in day 4 at move 1
No. 716 exposure increased to 2.0 in day 4 at 1
No. 732 exposure increased to 2.0 in day 4 at 1
No. 741 exposure increased to 4.0 in day 4 at 1
No. 743 exposure increased to 3.0 in day 4 at 1
No. 755 exposure increased to 3.0 in day 4 at 1
No. 765 exposure increased to 2.0 in day 4 at 1
No. 770 exposure increased to 4.0 in day 4 at 1
No. 777 exposure increased to 2.0 in day 4 at 1
No. 799 exposure increased to 3.0 in day 4 at 1
No. 800 exposure increased to 1.0 in day 4 at 1
No. 811 exposure increased to 3.0 in day 4 at 1
No. 822 exposure increased to 3.0 in day 4 at 1
No. 824 exposure increased to 1.0 in day 4 at 1
No. 835 exposure increased to 3.0 in day 4 at 1
No. 837 exposure increased to 2.0 in day 4 at 1
No. 848 exposure increased to 3.0 in day 4 at 1
No. 850 exposure increased to 3.0 in day 4 at 1
No. 870 exposure increased to 1.0 in day 4 at 1
No. 879 exposure increased to 3.0 in day 4 at 1
No. 885 exposure increased to 2.0 in day 4 at 1
No. 897 exposure increased to 2.0 in day 4 at 1
No. 901 exposure increased to 2.0 in day 4 at 1
No. 918 exposure increased to 3.0 in day 4 at 1
No. 919 exposure increased to 3.0 in day 4 at 1
No. 927 exposure increased to 3.0 in day 4 at 1
*When No. 936 infected, Exposure is 4.0 in day 4 at move 1
*When No. 942 infected, Exposure is 4.0 in day 4 at move 1
No. 944 exposure increased to 2.0 in day 4 at 1
No. 947 exposure increased to 2.0 in day 4 at 1
No. 952 exposure increased to 3.0 in day 4 at 1
No. 954 exposure increased to 1.0 in day 4 at 1
No. 981 exposure increased to 3.0 in day 4 at 1
No. 991 exposure increased to 2.0 in day 4 at 1
   23/10000 [..............................] - ETA: 30:59:11 - reward: 854.5261*When No. 25 infected, Exposure is 4.0 in day 4 at move 0
*When No. 182 infected, Exposure is 4.0 in day 4 at move 0
*When No. 254 infected, Exposure is 4.0 in day 4 at move 0
*When No. 306 infected, Exposure is 2.0 in day 4 at move 0
*When No. 383 infected, Exposure is 2.0 in day 4 at move 0
*When No. 401 infected, Exposure is 4.0 in day 4 at move 0
*When No. 453 infected, Exposure is 2.0 in day 4 at move 0
*When No. 454 infected, Exposure is 4.0 in day 4 at move 0
*When No. 455 infected, Exposure is 3.0 in day 4 at move 0
*When No. 467 infected, Exposure is 2.0 in day 4 at move 0
*When No. 524 infected, Exposure is 3.0 in day 4 at move 0
*When No. 664 infected, Exposure is 4.0 in day 4 at move 0
*When No. 770 infected, Exposure is 4.0 in day 4 at move 0
*When No. 850 infected, Exposure is 3.0 in day 4 at move 0
*When No. 901 infected, Exposure is 2.0 in day 4 at move 0
*When No. 944 infected, Exposure is 2.0 in day 4 at move 0
*When No. 67 infected, Exposure is 5.0 in day 4 at move 1
*When No. 189 infected, Exposure is 3.0 in day 4 at move 1
*When No. 211 infected, Exposure is 4.0 in day 4 at move 1
*When No. 300 infected, Exposure is 2.0 in day 4 at move 1
*When No. 438 infected, Exposure is 4.0 in day 4 at move 1
*When No. 525 infected, Exposure is 4.0 in day 4 at move 1
*When No. 659 infected, Exposure is 2.0 in day 4 at move 1
*When No. 799 infected, Exposure is 3.0 in day 4 at move 1
*When No. 848 infected, Exposure is 3.0 in day 4 at move 1
*When No. 919 infected, Exposure is 3.0 in day 4 at move 1
*When No. 927 infected, Exposure is 3.0 in day 4 at move 1
*When No. 952 infected, Exposure is 3.0 in day 4 at move 1
*When No. 5 infected, Exposure is 3.0 in day 4 at move 2
*When No. 14 infected, Exposure is 2.0 in day 4 at move 2
*When No. 54 infected, Exposure is 4.0 in day 4 at move 2
*When No. 152 infected, Exposure is 2.0 in day 4 at move 2
*When No. 258 infected, Exposure is 3.0 in day 4 at move 2
*When No. 370 infected, Exposure is 3.0 in day 4 at move 2
*When No. 456 infected, Exposure is 4.0 in day 4 at move 2
*When No. 536 infected, Exposure is 2.0 in day 4 at move 2
*When No. 716 infected, Exposure is 2.0 in day 4 at move 2
*When No. 741 infected, Exposure is 4.0 in day 4 at move 2
*When No. 777 infected, Exposure is 2.0 in day 4 at move 2
*When No. 811 infected, Exposure is 3.0 in day 4 at move 2
*When No. 835 infected, Exposure is 3.0 in day 4 at move 2
*When No. 981 infected, Exposure is 3.0 in day 4 at move 2
*When No. 126 infected, Exposure is 2.0 in day 4 at move 3
*When No. 150 infected, Exposure is 2.0 in day 4 at move 3
*When No. 205 infected, Exposure is 4.0 in day 4 at move 3
*When No. 365 infected, Exposure is 3.0 in day 4 at move 3
*When No. 419 infected, Exposure is 2.0 in day 4 at move 3
*When No. 478 infected, Exposure is 2.0 in day 4 at move 3
*When No. 743 infected, Exposure is 3.0 in day 4 at move 3
*When No. 755 infected, Exposure is 3.0 in day 4 at move 3
*When No. 149 infected, Exposure is 2.0 in day 4 at move 4
*When No. 283 infected, Exposure is 3.0 in day 4 at move 4
*When No. 382 infected, Exposure is 4.0 in day 4 at move 4
*When No. 490 infected, Exposure is 2.0 in day 4 at move 4
*When No. 662 infected, Exposure is 2.0 in day 4 at move 4
*When No. 991 infected, Exposure is 2.0 in day 4 at move 4
No. 15 exposure increased to 1.0 in day 4 at 5
No. 21 exposure increased to 3.0 in day 4 at 5
No. 31 exposure increased to 1.0 in day 4 at 5
No. 34 exposure increased to 2.0 in day 4 at 5
No. 38 exposure increased to 2.0 in day 4 at 5
No. 46 exposure increased to 1.0 in day 4 at 5
No. 49 exposure increased to 1.0 in day 4 at 5
No. 56 exposure increased to 1.0 in day 4 at 5
No. 58 exposure increased to 2.0 in day 4 at 5
No. 65 exposure increased to 1.0 in day 4 at 5
No. 72 exposure increased to 1.0 in day 4 at 5
No. 75 exposure increased to 1.0 in day 4 at 5
No. 78 exposure increased to 2.0 in day 4 at 5
No. 80 exposure increased to 4.0 in day 4 at 5
No. 86 exposure increased to 2.0 in day 4 at 5
No. 90 exposure increased to 4.0 in day 4 at 5
No. 97 exposure increased to 1.0 in day 4 at 5
No. 98 exposure increased to 1.0 in day 4 at 5
No. 99 exposure increased to 3.0 in day 4 at 5
No. 120 exposure increased to 1.0 in day 4 at 5
No. 124 exposure increased to 1.0 in day 4 at 5
No. 129 exposure increased to 1.0 in day 4 at 5
No. 140 exposure increased to 3.0 in day 4 at 5
No. 148 exposure increased to 3.0 in day 4 at 5
No. 158 exposure increased to 3.0 in day 4 at 5
No. 162 exposure increased to 2.0 in day 4 at 5
*When No. 164 infected, Exposure is 3.0 in day 4 at move 5
No. 175 exposure increased to 1.0 in day 4 at 5
No. 180 exposure increased to 2.0 in day 4 at 5
No. 186 exposure increased to 3.0 in day 4 at 5
No. 190 exposure increased to 3.0 in day 4 at 5
No. 213 exposure increased to 2.0 in day 4 at 5
No. 219 exposure increased to 1.0 in day 4 at 5
No. 223 exposure increased to 1.0 in day 4 at 5
No. 232 exposure increased to 1.0 in day 4 at 5
No. 236 exposure increased to 1.0 in day 4 at 5
No. 244 exposure increased to 1.0 in day 4 at 5
No. 262 exposure increased to 2.0 in day 4 at 5
No. 263 exposure increased to 3.0 in day 4 at 5
No. 285 exposure increased to 2.0 in day 4 at 5
No. 288 exposure increased to 2.0 in day 4 at 5
No. 305 exposure increased to 2.0 in day 4 at 5
No. 307 exposure increased to 1.0 in day 4 at 5
No. 315 exposure increased to 3.0 in day 4 at 5
No. 322 exposure increased to 1.0 in day 4 at 5
No. 329 exposure increased to 1.0 in day 4 at 5
No. 349 exposure increased to 2.0 in day 4 at 5
No. 351 exposure increased to 2.0 in day 4 at 5
No. 358 exposure increased to 2.0 in day 4 at 5
No. 366 exposure increased to 1.0 in day 4 at 5
No. 368 exposure increased to 2.0 in day 4 at 5
No. 373 exposure increased to 3.0 in day 4 at 5
No. 377 exposure increased to 2.0 in day 4 at 5
No. 380 exposure increased to 2.0 in day 4 at 5
No. 381 exposure increased to 2.0 in day 4 at 5
No. 392 exposure increased to 3.0 in day 4 at 5
No. 415 exposure increased to 1.0 in day 4 at 5
No. 417 exposure increased to 1.0 in day 4 at 5
No. 423 exposure increased to 3.0 in day 4 at 5
No. 425 exposure increased to 3.0 in day 4 at 5
No. 429 exposure increased to 3.0 in day 4 at 5
No. 430 exposure increased to 2.0 in day 4 at 5
No. 437 exposure increased to 3.0 in day 4 at 5
No. 439 exposure increased to 1.0 in day 4 at 5
No. 445 exposure increased to 3.0 in day 4 at 5
No. 463 exposure increased to 1.0 in day 4 at 5
No. 471 exposure increased to 1.0 in day 4 at 5
No. 494 exposure increased to 3.0 in day 4 at 5
No. 495 exposure increased to 1.0 in day 4 at 5
No. 496 exposure increased to 3.0 in day 4 at 5
No. 497 exposure increased to 1.0 in day 4 at 5
No. 499 exposure increased to 2.0 in day 4 at 5
No. 503 exposure increased to 4.0 in day 4 at 5
No. 509 exposure increased to 3.0 in day 4 at 5
No. 515 exposure increased to 1.0 in day 4 at 5
No. 516 exposure increased to 1.0 in day 4 at 5
No. 517 exposure increased to 3.0 in day 4 at 5
No. 539 exposure increased to 2.0 in day 4 at 5
No. 541 exposure increased to 1.0 in day 4 at 5
No. 553 exposure increased to 3.0 in day 4 at 5
No. 554 exposure increased to 2.0 in day 4 at 5
No. 557 exposure increased to 3.0 in day 4 at 5
No. 562 exposure increased to 3.0 in day 4 at 5
No. 566 exposure increased to 1.0 in day 4 at 5
No. 573 exposure increased to 1.0 in day 4 at 5
No. 579 exposure increased to 4.0 in day 4 at 5
*When No. 582 infected, Exposure is 3.0 in day 4 at move 5
No. 585 exposure increased to 1.0 in day 4 at 5
No. 586 exposure increased to 1.0 in day 4 at 5
No. 589 exposure increased to 3.0 in day 4 at 5
No. 592 exposure increased to 1.0 in day 4 at 5
No. 601 exposure increased to 1.0 in day 4 at 5
No. 610 exposure increased to 1.0 in day 4 at 5
No. 618 exposure increased to 2.0 in day 4 at 5
No. 629 exposure increased to 3.0 in day 4 at 5
No. 632 exposure increased to 1.0 in day 4 at 5
No. 634 exposure increased to 2.0 in day 4 at 5
No. 640 exposure increased to 1.0 in day 4 at 5
No. 646 exposure increased to 1.0 in day 4 at 5
No. 647 exposure increased to 2.0 in day 4 at 5
No. 649 exposure increased to 1.0 in day 4 at 5
No. 650 exposure increased to 3.0 in day 4 at 5
No. 653 exposure increased to 1.0 in day 4 at 5
No. 658 exposure increased to 1.0 in day 4 at 5
No. 661 exposure increased to 3.0 in day 4 at 5
No. 675 exposure increased to 3.0 in day 4 at 5
No. 684 exposure increased to 1.0 in day 4 at 5
No. 698 exposure increased to 3.0 in day 4 at 5
No. 701 exposure increased to 3.0 in day 4 at 5
No. 702 exposure increased to 3.0 in day 4 at 5
No. 719 exposure increased to 1.0 in day 4 at 5
No. 723 exposure increased to 1.0 in day 4 at 5
No. 727 exposure increased to 1.0 in day 4 at 5
No. 732 exposure increased to 3.0 in day 4 at 5
No. 736 exposure increased to 2.0 in day 4 at 5
No. 742 exposure increased to 2.0 in day 4 at 5
No. 765 exposure increased to 3.0 in day 4 at 5
No. 768 exposure increased to 1.0 in day 4 at 5
No. 771 exposure increased to 2.0 in day 4 at 5
No. 800 exposure increased to 2.0 in day 4 at 5
No. 804 exposure increased to 1.0 in day 4 at 5
No. 805 exposure increased to 1.0 in day 4 at 5
No. 815 exposure increased to 1.0 in day 4 at 5
No. 820 exposure increased to 2.0 in day 4 at 5
*When No. 822 infected, Exposure is 3.0 in day 4 at move 5
No. 824 exposure increased to 2.0 in day 4 at 5
No. 831 exposure increased to 1.0 in day 4 at 5
No. 836 exposure increased to 1.0 in day 4 at 5
No. 837 exposure increased to 3.0 in day 4 at 5
No. 840 exposure increased to 1.0 in day 4 at 5
No. 853 exposure increased to 1.0 in day 4 at 5
No. 859 exposure increased to 1.0 in day 4 at 5
No. 863 exposure increased to 1.0 in day 4 at 5
No. 870 exposure increased to 2.0 in day 4 at 5
No. 879 exposure increased to 4.0 in day 4 at 5
No. 885 exposure increased to 3.0 in day 4 at 5
No. 897 exposure increased to 3.0 in day 4 at 5
No. 916 exposure increased to 1.0 in day 4 at 5
No. 918 exposure increased to 4.0 in day 4 at 5
No. 940 exposure increased to 1.0 in day 4 at 5
No. 947 exposure increased to 3.0 in day 4 at 5
No. 949 exposure increased to 1.0 in day 4 at 5
No. 954 exposure increased to 2.0 in day 4 at 5
No. 961 exposure increased to 1.0 in day 4 at 5
No. 996 exposure increased to 1.0 in day 4 at 5
No. 997 exposure increased to 2.0 in day 4 at 5
   24/10000 [..............................] - ETA: 31:24:01 - reward: 845.6142*When No. 90 infected, Exposure is 4.0 in day 4 at move 0
*When No. 148 infected, Exposure is 3.0 in day 4 at move 0
*When No. 186 infected, Exposure is 3.0 in day 4 at move 0
*When No. 381 infected, Exposure is 2.0 in day 4 at move 0
*When No. 392 infected, Exposure is 3.0 in day 4 at move 0
*When No. 496 infected, Exposure is 3.0 in day 4 at move 0
*When No. 499 infected, Exposure is 2.0 in day 4 at move 0
*When No. 503 infected, Exposure is 4.0 in day 4 at move 0
*When No. 557 infected, Exposure is 3.0 in day 4 at move 0
*When No. 765 infected, Exposure is 3.0 in day 4 at move 0
*When No. 21 infected, Exposure is 3.0 in day 4 at move 1
*When No. 58 infected, Exposure is 2.0 in day 4 at move 1
*When No. 445 infected, Exposure is 3.0 in day 4 at move 1
*When No. 554 infected, Exposure is 2.0 in day 4 at move 1
*When No. 562 infected, Exposure is 3.0 in day 4 at move 1
*When No. 589 infected, Exposure is 3.0 in day 4 at move 1
*When No. 837 infected, Exposure is 3.0 in day 4 at move 1
*When No. 954 infected, Exposure is 2.0 in day 4 at move 1
*When No. 140 infected, Exposure is 3.0 in day 4 at move 2
*When No. 349 infected, Exposure is 2.0 in day 4 at move 2
*When No. 425 infected, Exposure is 3.0 in day 4 at move 2
*When No. 539 infected, Exposure is 2.0 in day 4 at move 2
*When No. 579 infected, Exposure is 4.0 in day 4 at move 2
*When No. 634 infected, Exposure is 2.0 in day 4 at move 2
*When No. 650 infected, Exposure is 3.0 in day 4 at move 2
*When No. 675 infected, Exposure is 3.0 in day 4 at move 2
*When No. 879 infected, Exposure is 4.0 in day 4 at move 2
*When No. 34 infected, Exposure is 2.0 in day 4 at move 3
*When No. 80 infected, Exposure is 4.0 in day 4 at move 3
*When No. 430 infected, Exposure is 2.0 in day 4 at move 3
*When No. 702 infected, Exposure is 3.0 in day 4 at move 3
*When No. 800 infected, Exposure is 2.0 in day 4 at move 3
*When No. 824 infected, Exposure is 2.0 in day 4 at move 3
*When No. 870 infected, Exposure is 2.0 in day 4 at move 3
*When No. 947 infected, Exposure is 3.0 in day 4 at move 3
*When No. 263 infected, Exposure is 3.0 in day 4 at move 4
*When No. 429 infected, Exposure is 3.0 in day 4 at move 4
*When No. 517 infected, Exposure is 3.0 in day 4 at move 4
*When No. 629 infected, Exposure is 3.0 in day 4 at move 4
*When No. 661 infected, Exposure is 3.0 in day 4 at move 4
*When No. 701 infected, Exposure is 3.0 in day 4 at move 4
*When No. 918 infected, Exposure is 4.0 in day 4 at move 4
No. 1 exposure increased to 2.0 in day 4 at 5
No. 7 exposure increased to 1.0 in day 4 at 5
No. 11 exposure increased to 2.0 in day 4 at 5
No. 15 exposure increased to 2.0 in day 4 at 5
No. 17 exposure increased to 1.0 in day 4 at 5
No. 31 exposure increased to 2.0 in day 4 at 5
No. 38 exposure increased to 3.0 in day 4 at 5
No. 43 exposure increased to 2.0 in day 4 at 5
No. 46 exposure increased to 2.0 in day 4 at 5
No. 47 exposure increased to 2.0 in day 4 at 5
No. 49 exposure increased to 2.0 in day 4 at 5
No. 56 exposure increased to 2.0 in day 4 at 5
No. 60 exposure increased to 1.0 in day 4 at 5
No. 65 exposure increased to 2.0 in day 4 at 5
No. 72 exposure increased to 2.0 in day 4 at 5
No. 75 exposure increased to 2.0 in day 4 at 5
No. 78 exposure increased to 3.0 in day 4 at 5
No. 86 exposure increased to 3.0 in day 4 at 5
No. 97 exposure increased to 2.0 in day 4 at 5
No. 98 exposure increased to 2.0 in day 4 at 5
No. 99 exposure increased to 4.0 in day 4 at 5
No. 120 exposure increased to 2.0 in day 4 at 5
No. 124 exposure increased to 2.0 in day 4 at 5
No. 129 exposure increased to 2.0 in day 4 at 5
No. 147 exposure increased to 1.0 in day 4 at 5
No. 154 exposure increased to 1.0 in day 4 at 5
No. 158 exposure increased to 4.0 in day 4 at 5
No. 162 exposure increased to 3.0 in day 4 at 5
No. 175 exposure increased to 2.0 in day 4 at 5
No. 178 exposure increased to 1.0 in day 4 at 5
No. 180 exposure increased to 3.0 in day 4 at 5
No. 184 exposure increased to 1.0 in day 4 at 5
*When No. 190 infected, Exposure is 3.0 in day 4 at move 5
No. 199 exposure increased to 1.0 in day 4 at 5
No. 213 exposure increased to 3.0 in day 4 at 5
No. 219 exposure increased to 2.0 in day 4 at 5
No. 221 exposure increased to 1.0 in day 4 at 5
No. 223 exposure increased to 2.0 in day 4 at 5
No. 232 exposure increased to 2.0 in day 4 at 5
No. 236 exposure increased to 2.0 in day 4 at 5
No. 244 exposure increased to 2.0 in day 4 at 5
No. 262 exposure increased to 3.0 in day 4 at 5
No. 269 exposure increased to 1.0 in day 4 at 5
No. 271 exposure increased to 1.0 in day 4 at 5
No. 285 exposure increased to 3.0 in day 4 at 5
*When No. 288 infected, Exposure is 2.0 in day 4 at move 5
No. 302 exposure increased to 1.0 in day 4 at 5
No. 305 exposure increased to 3.0 in day 4 at 5
No. 307 exposure increased to 2.0 in day 4 at 5
No. 315 exposure increased to 4.0 in day 4 at 5
No. 321 exposure increased to 1.0 in day 4 at 5
No. 322 exposure increased to 2.0 in day 4 at 5
No. 328 exposure increased to 1.0 in day 4 at 5
No. 329 exposure increased to 2.0 in day 4 at 5
No. 351 exposure increased to 3.0 in day 4 at 5
No. 358 exposure increased to 3.0 in day 4 at 5
No. 366 exposure increased to 2.0 in day 4 at 5
No. 368 exposure increased to 3.0 in day 4 at 5
*When No. 373 infected, Exposure is 3.0 in day 4 at move 5
No. 377 exposure increased to 3.0 in day 4 at 5
No. 380 exposure increased to 3.0 in day 4 at 5
No. 404 exposure increased to 1.0 in day 4 at 5
No. 408 exposure increased to 1.0 in day 4 at 5
No. 415 exposure increased to 2.0 in day 4 at 5
No. 417 exposure increased to 2.0 in day 4 at 5
No. 423 exposure increased to 4.0 in day 4 at 5
No. 427 exposure increased to 1.0 in day 4 at 5
No. 437 exposure increased to 4.0 in day 4 at 5
No. 439 exposure increased to 2.0 in day 4 at 5
No. 447 exposure increased to 2.0 in day 4 at 5
No. 463 exposure increased to 2.0 in day 4 at 5
No. 464 exposure increased to 1.0 in day 4 at 5
No. 471 exposure increased to 2.0 in day 4 at 5
No. 484 exposure increased to 1.0 in day 4 at 5
No. 494 exposure increased to 4.0 in day 4 at 5
No. 495 exposure increased to 2.0 in day 4 at 5
No. 497 exposure increased to 2.0 in day 4 at 5
No. 509 exposure increased to 4.0 in day 4 at 5
No. 512 exposure increased to 1.0 in day 4 at 5
No. 515 exposure increased to 2.0 in day 4 at 5
No. 516 exposure increased to 2.0 in day 4 at 5
No. 541 exposure increased to 2.0 in day 4 at 5
No. 546 exposure increased to 1.0 in day 4 at 5
No. 553 exposure increased to 4.0 in day 4 at 5
No. 556 exposure increased to 1.0 in day 4 at 5
No. 559 exposure increased to 1.0 in day 4 at 5
No. 566 exposure increased to 2.0 in day 4 at 5
No. 573 exposure increased to 2.0 in day 4 at 5
No. 583 exposure increased to 2.0 in day 4 at 5
No. 585 exposure increased to 2.0 in day 4 at 5
No. 586 exposure increased to 2.0 in day 4 at 5
No. 592 exposure increased to 2.0 in day 4 at 5
No. 601 exposure increased to 2.0 in day 4 at 5
No. 606 exposure increased to 1.0 in day 4 at 5
No. 610 exposure increased to 2.0 in day 4 at 5
No. 618 exposure increased to 3.0 in day 4 at 5
No. 632 exposure increased to 2.0 in day 4 at 5
No. 640 exposure increased to 2.0 in day 4 at 5
No. 645 exposure increased to 2.0 in day 4 at 5
No. 646 exposure increased to 2.0 in day 4 at 5
No. 647 exposure increased to 3.0 in day 4 at 5
No. 649 exposure increased to 2.0 in day 4 at 5
No. 653 exposure increased to 2.0 in day 4 at 5
No. 658 exposure increased to 2.0 in day 4 at 5
No. 667 exposure increased to 1.0 in day 4 at 5
No. 684 exposure increased to 2.0 in day 4 at 5
No. 698 exposure increased to 4.0 in day 4 at 5
No. 714 exposure increased to 1.0 in day 4 at 5
No. 719 exposure increased to 2.0 in day 4 at 5
No. 723 exposure increased to 2.0 in day 4 at 5
No. 727 exposure increased to 2.0 in day 4 at 5
*When No. 732 infected, Exposure is 3.0 in day 4 at move 5
No. 736 exposure increased to 3.0 in day 4 at 5
No. 742 exposure increased to 3.0 in day 4 at 5
No. 757 exposure increased to 1.0 in day 4 at 5
No. 762 exposure increased to 1.0 in day 4 at 5
No. 766 exposure increased to 1.0 in day 4 at 5
No. 768 exposure increased to 2.0 in day 4 at 5
No. 771 exposure increased to 3.0 in day 4 at 5
No. 774 exposure increased to 1.0 in day 4 at 5
No. 781 exposure increased to 1.0 in day 4 at 5
No. 786 exposure increased to 1.0 in day 4 at 5
No. 796 exposure increased to 1.0 in day 4 at 5
No. 801 exposure increased to 1.0 in day 4 at 5
No. 804 exposure increased to 2.0 in day 4 at 5
No. 805 exposure increased to 2.0 in day 4 at 5
No. 815 exposure increased to 2.0 in day 4 at 5
No. 820 exposure increased to 3.0 in day 4 at 5
No. 831 exposure increased to 2.0 in day 4 at 5
No. 836 exposure increased to 2.0 in day 4 at 5
No. 840 exposure increased to 2.0 in day 4 at 5
No. 853 exposure increased to 2.0 in day 4 at 5
No. 859 exposure increased to 2.0 in day 4 at 5
No. 862 exposure increased to 1.0 in day 4 at 5
No. 863 exposure increased to 2.0 in day 4 at 5
No. 885 exposure increased to 4.0 in day 4 at 5
No. 897 exposure increased to 4.0 in day 4 at 5
No. 902 exposure increased to 1.0 in day 4 at 5
No. 916 exposure increased to 2.0 in day 4 at 5
No. 925 exposure increased to 1.0 in day 4 at 5
No. 928 exposure increased to 1.0 in day 4 at 5
No. 930 exposure increased to 1.0 in day 4 at 5
No. 940 exposure increased to 2.0 in day 4 at 5
No. 949 exposure increased to 2.0 in day 4 at 5
No. 950 exposure increased to 1.0 in day 4 at 5
No. 961 exposure increased to 2.0 in day 4 at 5
No. 963 exposure increased to 1.0 in day 4 at 5
No. 970 exposure increased to 1.0 in day 4 at 5
No. 994 exposure increased to 1.0 in day 4 at 5
No. 996 exposure increased to 2.0 in day 4 at 5
No. 997 exposure increased to 3.0 in day 4 at 5
No. 998 exposure increased to 1.0 in day 4 at 5
   25/10000 [..............................] - ETA: 31:42:32 - reward: 837.4328*When No. 46 infected, Exposure is 2.0 in day 4 at move 0
*When No. 56 infected, Exposure is 2.0 in day 4 at move 0
*When No. 99 infected, Exposure is 4.0 in day 4 at move 0
*When No. 158 infected, Exposure is 4.0 in day 4 at move 0
*When No. 232 infected, Exposure is 2.0 in day 4 at move 0
*When No. 423 infected, Exposure is 4.0 in day 4 at move 0
*When No. 437 infected, Exposure is 4.0 in day 4 at move 0
*When No. 494 infected, Exposure is 4.0 in day 4 at move 0
*When No. 647 infected, Exposure is 3.0 in day 4 at move 0
*When No. 698 infected, Exposure is 4.0 in day 4 at move 0
*When No. 804 infected, Exposure is 2.0 in day 4 at move 0
*When No. 1 infected, Exposure is 2.0 in day 4 at move 1
*When No. 49 infected, Exposure is 2.0 in day 4 at move 1
*When No. 72 infected, Exposure is 2.0 in day 4 at move 1
*When No. 78 infected, Exposure is 3.0 in day 4 at move 1
*When No. 129 infected, Exposure is 2.0 in day 4 at move 1
*When No. 180 infected, Exposure is 3.0 in day 4 at move 1
*When No. 219 infected, Exposure is 2.0 in day 4 at move 1
*When No. 285 infected, Exposure is 3.0 in day 4 at move 1
*When No. 315 infected, Exposure is 4.0 in day 4 at move 1
*When No. 322 infected, Exposure is 2.0 in day 4 at move 1
*When No. 351 infected, Exposure is 3.0 in day 4 at move 1
*When No. 380 infected, Exposure is 3.0 in day 4 at move 1
*When No. 463 infected, Exposure is 2.0 in day 4 at move 1
*When No. 509 infected, Exposure is 4.0 in day 4 at move 1
*When No. 553 infected, Exposure is 4.0 in day 4 at move 1
*When No. 719 infected, Exposure is 2.0 in day 4 at move 1
*When No. 723 infected, Exposure is 2.0 in day 4 at move 1
*When No. 771 infected, Exposure is 3.0 in day 4 at move 1
*When No. 820 infected, Exposure is 3.0 in day 4 at move 1
*When No. 885 infected, Exposure is 4.0 in day 4 at move 1
*When No. 996 infected, Exposure is 2.0 in day 4 at move 1
*When No. 997 infected, Exposure is 3.0 in day 4 at move 1
*When No. 97 infected, Exposure is 2.0 in day 4 at move 2
*When No. 262 infected, Exposure is 3.0 in day 4 at move 2
*When No. 541 infected, Exposure is 2.0 in day 4 at move 2
*When No. 742 infected, Exposure is 3.0 in day 4 at move 2
*When No. 831 infected, Exposure is 2.0 in day 4 at move 2
*When No. 236 infected, Exposure is 2.0 in day 4 at move 3
*When No. 586 infected, Exposure is 2.0 in day 4 at move 3
*When No. 618 infected, Exposure is 3.0 in day 4 at move 3
*When No. 646 infected, Exposure is 2.0 in day 4 at move 3
*When No. 897 infected, Exposure is 4.0 in day 4 at move 3
*When No. 75 infected, Exposure is 2.0 in day 4 at move 4
*When No. 98 infected, Exposure is 2.0 in day 4 at move 4
*When No. 213 infected, Exposure is 3.0 in day 4 at move 4
*When No. 307 infected, Exposure is 2.0 in day 4 at move 4
*When No. 417 infected, Exposure is 2.0 in day 4 at move 4
*When No. 585 infected, Exposure is 2.0 in day 4 at move 4
*When No. 601 infected, Exposure is 2.0 in day 4 at move 4
*When No. 632 infected, Exposure is 2.0 in day 4 at move 4
*When No. 653 infected, Exposure is 2.0 in day 4 at move 4
*When No. 805 infected, Exposure is 2.0 in day 4 at move 4
No. 2 exposure increased to 1.0 in day 4 at 5
No. 4 exposure increased to 1.0 in day 4 at 5
No. 7 exposure increased to 2.0 in day 4 at 5
No. 11 exposure increased to 3.0 in day 4 at 5
No. 15 exposure increased to 3.0 in day 4 at 5
No. 17 exposure increased to 2.0 in day 4 at 5
No. 27 exposure increased to 1.0 in day 4 at 5
No. 31 exposure increased to 3.0 in day 4 at 5
No. 38 exposure increased to 4.0 in day 4 at 5
No. 43 exposure increased to 3.0 in day 4 at 5
No. 47 exposure increased to 3.0 in day 4 at 5
No. 60 exposure increased to 2.0 in day 4 at 5
No. 65 exposure increased to 3.0 in day 4 at 5
No. 73 exposure increased to 1.0 in day 4 at 5
No. 79 exposure increased to 1.0 in day 4 at 5
No. 84 exposure increased to 1.0 in day 4 at 5
No. 86 exposure increased to 4.0 in day 4 at 5
No. 104 exposure increased to 1.0 in day 4 at 5
No. 115 exposure increased to 1.0 in day 4 at 5
No. 116 exposure increased to 1.0 in day 4 at 5
*When No. 120 infected, Exposure is 2.0 in day 4 at move 5
*When No. 124 infected, Exposure is 2.0 in day 4 at move 5
No. 130 exposure increased to 1.0 in day 4 at 5
No. 147 exposure increased to 2.0 in day 4 at 5
No. 154 exposure increased to 2.0 in day 4 at 5
No. 162 exposure increased to 4.0 in day 4 at 5
No. 175 exposure increased to 3.0 in day 4 at 5
No. 178 exposure increased to 2.0 in day 4 at 5
No. 184 exposure increased to 2.0 in day 4 at 5
No. 197 exposure increased to 1.0 in day 4 at 5
No. 199 exposure increased to 2.0 in day 4 at 5
No. 214 exposure increased to 1.0 in day 4 at 5
No. 217 exposure increased to 1.0 in day 4 at 5
No. 221 exposure increased to 2.0 in day 4 at 5
No. 223 exposure increased to 3.0 in day 4 at 5
No. 227 exposure increased to 1.0 in day 4 at 5
No. 244 exposure increased to 3.0 in day 4 at 5
No. 269 exposure increased to 2.0 in day 4 at 5
No. 271 exposure increased to 2.0 in day 4 at 5
No. 295 exposure increased to 1.0 in day 4 at 5
No. 296 exposure increased to 1.0 in day 4 at 5
No. 302 exposure increased to 2.0 in day 4 at 5
*When No. 305 infected, Exposure is 3.0 in day 4 at move 5
No. 311 exposure increased to 1.0 in day 4 at 5
No. 321 exposure increased to 2.0 in day 4 at 5
No. 328 exposure increased to 2.0 in day 4 at 5
No. 329 exposure increased to 3.0 in day 4 at 5
No. 358 exposure increased to 4.0 in day 4 at 5
No. 359 exposure increased to 1.0 in day 4 at 5
No. 361 exposure increased to 2.0 in day 4 at 5
No. 364 exposure increased to 1.0 in day 4 at 5
No. 366 exposure increased to 3.0 in day 4 at 5
No. 368 exposure increased to 4.0 in day 4 at 5
No. 376 exposure increased to 2.0 in day 4 at 5
No. 377 exposure increased to 4.0 in day 4 at 5
No. 394 exposure increased to 1.0 in day 4 at 5
No. 396 exposure increased to 1.0 in day 4 at 5
No. 404 exposure increased to 2.0 in day 4 at 5
No. 405 exposure increased to 1.0 in day 4 at 5
No. 408 exposure increased to 2.0 in day 4 at 5
No. 415 exposure increased to 3.0 in day 4 at 5
No. 427 exposure increased to 2.0 in day 4 at 5
No. 439 exposure increased to 3.0 in day 4 at 5
No. 447 exposure increased to 3.0 in day 4 at 5
No. 464 exposure increased to 2.0 in day 4 at 5
No. 471 exposure increased to 3.0 in day 4 at 5
No. 473 exposure increased to 1.0 in day 4 at 5
No. 476 exposure increased to 1.0 in day 4 at 5
No. 481 exposure increased to 1.0 in day 4 at 5
No. 484 exposure increased to 2.0 in day 4 at 5
No. 485 exposure increased to 1.0 in day 4 at 5
No. 495 exposure increased to 3.0 in day 4 at 5
No. 497 exposure increased to 3.0 in day 4 at 5
No. 512 exposure increased to 2.0 in day 4 at 5
No. 513 exposure increased to 1.0 in day 4 at 5
No. 515 exposure increased to 3.0 in day 4 at 5
No. 516 exposure increased to 3.0 in day 4 at 5
No. 546 exposure increased to 2.0 in day 4 at 5
No. 556 exposure increased to 2.0 in day 4 at 5
No. 559 exposure increased to 2.0 in day 4 at 5
No. 566 exposure increased to 3.0 in day 4 at 5
No. 568 exposure increased to 1.0 in day 4 at 5
No. 570 exposure increased to 2.0 in day 4 at 5
No. 573 exposure increased to 3.0 in day 4 at 5
No. 577 exposure increased to 1.0 in day 4 at 5
No. 580 exposure increased to 1.0 in day 4 at 5
No. 583 exposure increased to 3.0 in day 4 at 5
No. 592 exposure increased to 3.0 in day 4 at 5
No. 598 exposure increased to 1.0 in day 4 at 5
No. 600 exposure increased to 1.0 in day 4 at 5
No. 606 exposure increased to 2.0 in day 4 at 5
No. 610 exposure increased to 3.0 in day 4 at 5
No. 616 exposure increased to 1.0 in day 4 at 5
No. 630 exposure increased to 1.0 in day 4 at 5
No. 640 exposure increased to 3.0 in day 4 at 5
No. 642 exposure increased to 1.0 in day 4 at 5
No. 645 exposure increased to 3.0 in day 4 at 5
No. 649 exposure increased to 3.0 in day 4 at 5
*When No. 658 infected, Exposure is 2.0 in day 4 at move 5
No. 667 exposure increased to 2.0 in day 4 at 5
No. 669 exposure increased to 1.0 in day 4 at 5
No. 678 exposure increased to 1.0 in day 4 at 5
No. 682 exposure increased to 1.0 in day 4 at 5
No. 684 exposure increased to 3.0 in day 4 at 5
No. 685 exposure increased to 1.0 in day 4 at 5
No. 714 exposure increased to 2.0 in day 4 at 5
No. 727 exposure increased to 3.0 in day 4 at 5
No. 730 exposure increased to 1.0 in day 4 at 5
No. 736 exposure increased to 4.0 in day 4 at 5
No. 739 exposure increased to 1.0 in day 4 at 5
No. 757 exposure increased to 2.0 in day 4 at 5
No. 762 exposure increased to 2.0 in day 4 at 5
No. 763 exposure increased to 2.0 in day 4 at 5
No. 766 exposure increased to 2.0 in day 4 at 5
No. 768 exposure increased to 3.0 in day 4 at 5
No. 769 exposure increased to 1.0 in day 4 at 5
No. 772 exposure increased to 1.0 in day 4 at 5
No. 774 exposure increased to 2.0 in day 4 at 5
No. 779 exposure increased to 1.0 in day 4 at 5
No. 781 exposure increased to 2.0 in day 4 at 5
No. 786 exposure increased to 2.0 in day 4 at 5
No. 789 exposure increased to 1.0 in day 4 at 5
No. 796 exposure increased to 2.0 in day 4 at 5
No. 801 exposure increased to 2.0 in day 4 at 5
No. 802 exposure increased to 1.0 in day 4 at 5
No. 807 exposure increased to 1.0 in day 4 at 5
No. 815 exposure increased to 3.0 in day 4 at 5
No. 821 exposure increased to 1.0 in day 4 at 5
No. 827 exposure increased to 1.0 in day 4 at 5
No. 828 exposure increased to 1.0 in day 4 at 5
No. 836 exposure increased to 3.0 in day 4 at 5
No. 840 exposure increased to 3.0 in day 4 at 5
No. 853 exposure increased to 3.0 in day 4 at 5
No. 859 exposure increased to 3.0 in day 4 at 5
No. 862 exposure increased to 2.0 in day 4 at 5
*When No. 863 infected, Exposure is 2.0 in day 4 at move 5
No. 865 exposure increased to 1.0 in day 4 at 5
No. 869 exposure increased to 1.0 in day 4 at 5
No. 873 exposure increased to 1.0 in day 4 at 5
No. 877 exposure increased to 1.0 in day 4 at 5
No. 888 exposure increased to 1.0 in day 4 at 5
No. 898 exposure increased to 1.0 in day 4 at 5
No. 902 exposure increased to 2.0 in day 4 at 5
No. 912 exposure increased to 1.0 in day 4 at 5
No. 916 exposure increased to 3.0 in day 4 at 5
No. 925 exposure increased to 2.0 in day 4 at 5
No. 928 exposure increased to 2.0 in day 4 at 5
No. 930 exposure increased to 2.0 in day 4 at 5
No. 933 exposure increased to 1.0 in day 4 at 5
No. 939 exposure increased to 1.0 in day 4 at 5
No. 940 exposure increased to 3.0 in day 4 at 5
No. 943 exposure increased to 1.0 in day 4 at 5
No. 949 exposure increased to 3.0 in day 4 at 5
No. 950 exposure increased to 2.0 in day 4 at 5
No. 958 exposure increased to 1.0 in day 4 at 5
No. 961 exposure increased to 3.0 in day 4 at 5
No. 963 exposure increased to 2.0 in day 4 at 5
No. 964 exposure increased to 1.0 in day 4 at 5
No. 970 exposure increased to 2.0 in day 4 at 5
No. 973 exposure increased to 2.0 in day 4 at 5
No. 984 exposure increased to 1.0 in day 4 at 5
No. 994 exposure increased to 2.0 in day 4 at 5
No. 998 exposure increased to 2.0 in day 4 at 5
   26/10000 [..............................] - ETA: 31:54:57 - reward: 824.5162*When No. 15 infected, Exposure is 3.0 in day 4 at move 0
*When No. 31 infected, Exposure is 3.0 in day 4 at move 0
*When No. 162 infected, Exposure is 4.0 in day 4 at move 0
*When No. 221 infected, Exposure is 2.0 in day 4 at move 0
*When No. 377 infected, Exposure is 4.0 in day 4 at move 0
*When No. 404 infected, Exposure is 2.0 in day 4 at move 0
*When No. 471 infected, Exposure is 3.0 in day 4 at move 0
*When No. 495 infected, Exposure is 3.0 in day 4 at move 0
*When No. 556 infected, Exposure is 2.0 in day 4 at move 0
*When No. 566 infected, Exposure is 3.0 in day 4 at move 0
*When No. 573 infected, Exposure is 3.0 in day 4 at move 0
*When No. 606 infected, Exposure is 2.0 in day 4 at move 0
*When No. 640 infected, Exposure is 3.0 in day 4 at move 0
*When No. 684 infected, Exposure is 3.0 in day 4 at move 0
*When No. 714 infected, Exposure is 2.0 in day 4 at move 0
*When No. 801 infected, Exposure is 2.0 in day 4 at move 0
*When No. 940 infected, Exposure is 3.0 in day 4 at move 0
*When No. 949 infected, Exposure is 3.0 in day 4 at move 0
*When No. 184 infected, Exposure is 2.0 in day 4 at move 1
*When No. 358 infected, Exposure is 4.0 in day 4 at move 1
*When No. 439 infected, Exposure is 3.0 in day 4 at move 1
*When No. 516 infected, Exposure is 3.0 in day 4 at move 1
*When No. 570 infected, Exposure is 2.0 in day 4 at move 1
*When No. 727 infected, Exposure is 3.0 in day 4 at move 1
*When No. 766 infected, Exposure is 2.0 in day 4 at move 1
*When No. 950 infected, Exposure is 2.0 in day 4 at move 1
*When No. 970 infected, Exposure is 2.0 in day 4 at move 1
*When No. 328 infected, Exposure is 2.0 in day 4 at move 2
*When No. 515 infected, Exposure is 3.0 in day 4 at move 2
*When No. 768 infected, Exposure is 3.0 in day 4 at move 2
*When No. 916 infected, Exposure is 3.0 in day 4 at move 2
*When No. 47 infected, Exposure is 3.0 in day 4 at move 3
*When No. 60 infected, Exposure is 2.0 in day 4 at move 3
*When No. 65 infected, Exposure is 3.0 in day 4 at move 3
*When No. 178 infected, Exposure is 2.0 in day 4 at move 3
*When No. 321 infected, Exposure is 2.0 in day 4 at move 3
*When No. 366 infected, Exposure is 3.0 in day 4 at move 3
*When No. 376 infected, Exposure is 2.0 in day 4 at move 3
*When No. 649 infected, Exposure is 3.0 in day 4 at move 3
*When No. 840 infected, Exposure is 3.0 in day 4 at move 3
*When No. 43 infected, Exposure is 3.0 in day 4 at move 4
*When No. 86 infected, Exposure is 4.0 in day 4 at move 4
*When No. 368 infected, Exposure is 4.0 in day 4 at move 4
*When No. 408 infected, Exposure is 2.0 in day 4 at move 4
*When No. 415 infected, Exposure is 3.0 in day 4 at move 4
*When No. 484 infected, Exposure is 2.0 in day 4 at move 4
*When No. 610 infected, Exposure is 3.0 in day 4 at move 4
*When No. 763 infected, Exposure is 2.0 in day 4 at move 4
*When No. 836 infected, Exposure is 3.0 in day 4 at move 4
*When No. 853 infected, Exposure is 3.0 in day 4 at move 4
*When No. 859 infected, Exposure is 3.0 in day 4 at move 4
*When No. 994 infected, Exposure is 2.0 in day 4 at move 4
No. 2 exposure increased to 2.0 in day 4 at 5
No. 4 exposure increased to 2.0 in day 4 at 5
No. 7 exposure increased to 3.0 in day 4 at 5
*When No. 11 infected, Exposure is 3.0 in day 4 at move 5
No. 17 exposure increased to 3.0 in day 4 at 5
No. 20 exposure increased to 2.0 in day 4 at 5
No. 27 exposure increased to 2.0 in day 4 at 5
No. 38 exposure increased to 5.0 in day 4 at 5
No. 40 exposure increased to 1.0 in day 4 at 5
No. 63 exposure increased to 1.0 in day 4 at 5
No. 73 exposure increased to 2.0 in day 4 at 5
No. 79 exposure increased to 2.0 in day 4 at 5
No. 84 exposure increased to 2.0 in day 4 at 5
No. 93 exposure increased to 1.0 in day 4 at 5
No. 104 exposure increased to 2.0 in day 4 at 5
No. 109 exposure increased to 1.0 in day 4 at 5
No. 115 exposure increased to 2.0 in day 4 at 5
No. 116 exposure increased to 2.0 in day 4 at 5
No. 117 exposure increased to 2.0 in day 4 at 5
No. 130 exposure increased to 2.0 in day 4 at 5
No. 132 exposure increased to 1.0 in day 4 at 5
No. 133 exposure increased to 1.0 in day 4 at 5
No. 147 exposure increased to 3.0 in day 4 at 5
No. 151 exposure increased to 1.0 in day 4 at 5
No. 154 exposure increased to 3.0 in day 4 at 5
No. 156 exposure increased to 2.0 in day 4 at 5
No. 175 exposure increased to 4.0 in day 4 at 5
No. 179 exposure increased to 1.0 in day 4 at 5
No. 197 exposure increased to 2.0 in day 4 at 5
No. 198 exposure increased to 1.0 in day 4 at 5
No. 199 exposure increased to 3.0 in day 4 at 5
No. 203 exposure increased to 2.0 in day 4 at 5
No. 214 exposure increased to 2.0 in day 4 at 5
No. 217 exposure increased to 2.0 in day 4 at 5
*When No. 223 infected, Exposure is 3.0 in day 4 at move 5
No. 227 exposure increased to 2.0 in day 4 at 5
No. 233 exposure increased to 1.0 in day 4 at 5
No. 241 exposure increased to 1.0 in day 4 at 5
No. 244 exposure increased to 4.0 in day 4 at 5
No. 245 exposure increased to 1.0 in day 4 at 5
No. 265 exposure increased to 1.0 in day 4 at 5
No. 266 exposure increased to 1.0 in day 4 at 5
No. 268 exposure increased to 1.0 in day 4 at 5
No. 269 exposure increased to 3.0 in day 4 at 5
No. 271 exposure increased to 3.0 in day 4 at 5
No. 281 exposure increased to 1.0 in day 4 at 5
No. 284 exposure increased to 1.0 in day 4 at 5
No. 294 exposure increased to 1.0 in day 4 at 5
No. 295 exposure increased to 2.0 in day 4 at 5
No. 296 exposure increased to 2.0 in day 4 at 5
No. 297 exposure increased to 1.0 in day 4 at 5
No. 302 exposure increased to 3.0 in day 4 at 5
No. 310 exposure increased to 2.0 in day 4 at 5
No. 311 exposure increased to 2.0 in day 4 at 5
No. 316 exposure increased to 2.0 in day 4 at 5
No. 325 exposure increased to 2.0 in day 4 at 5
No. 329 exposure increased to 4.0 in day 4 at 5
No. 359 exposure increased to 2.0 in day 4 at 5
No. 361 exposure increased to 3.0 in day 4 at 5
No. 364 exposure increased to 2.0 in day 4 at 5
No. 394 exposure increased to 2.0 in day 4 at 5
No. 395 exposure increased to 1.0 in day 4 at 5
No. 396 exposure increased to 2.0 in day 4 at 5
No. 405 exposure increased to 2.0 in day 4 at 5
No. 420 exposure increased to 1.0 in day 4 at 5
No. 427 exposure increased to 3.0 in day 4 at 5
No. 436 exposure increased to 1.0 in day 4 at 5
No. 447 exposure increased to 4.0 in day 4 at 5
No. 459 exposure increased to 1.0 in day 4 at 5
No. 464 exposure increased to 3.0 in day 4 at 5
No. 473 exposure increased to 2.0 in day 4 at 5
No. 476 exposure increased to 2.0 in day 4 at 5
No. 481 exposure increased to 2.0 in day 4 at 5
No. 485 exposure increased to 2.0 in day 4 at 5
No. 489 exposure increased to 2.0 in day 4 at 5
*When No. 497 infected, Exposure is 3.0 in day 4 at move 5
No. 512 exposure increased to 3.0 in day 4 at 5
No. 513 exposure increased to 2.0 in day 4 at 5
No. 518 exposure increased to 1.0 in day 4 at 5
No. 526 exposure increased to 1.0 in day 4 at 5
No. 529 exposure increased to 1.0 in day 4 at 5
No. 535 exposure increased to 1.0 in day 4 at 5
No. 545 exposure increased to 2.0 in day 4 at 5
No. 546 exposure increased to 3.0 in day 4 at 5
No. 559 exposure increased to 3.0 in day 4 at 5
No. 567 exposure increased to 1.0 in day 4 at 5
No. 568 exposure increased to 2.0 in day 4 at 5
No. 569 exposure increased to 1.0 in day 4 at 5
No. 577 exposure increased to 2.0 in day 4 at 5
No. 580 exposure increased to 2.0 in day 4 at 5
No. 583 exposure increased to 4.0 in day 4 at 5
*When No. 592 infected, Exposure is 3.0 in day 4 at move 5
No. 598 exposure increased to 2.0 in day 4 at 5
No. 600 exposure increased to 2.0 in day 4 at 5
No. 604 exposure increased to 2.0 in day 4 at 5
No. 605 exposure increased to 1.0 in day 4 at 5
No. 616 exposure increased to 2.0 in day 4 at 5
No. 619 exposure increased to 1.0 in day 4 at 5
No. 630 exposure increased to 2.0 in day 4 at 5
No. 641 exposure increased to 1.0 in day 4 at 5
No. 642 exposure increased to 2.0 in day 4 at 5
No. 645 exposure increased to 4.0 in day 4 at 5
No. 655 exposure increased to 1.0 in day 4 at 5
No. 667 exposure increased to 3.0 in day 4 at 5
No. 669 exposure increased to 2.0 in day 4 at 5
No. 678 exposure increased to 2.0 in day 4 at 5
No. 680 exposure increased to 1.0 in day 4 at 5
No. 682 exposure increased to 2.0 in day 4 at 5
No. 685 exposure increased to 2.0 in day 4 at 5
No. 703 exposure increased to 2.0 in day 4 at 5
No. 712 exposure increased to 1.0 in day 4 at 5
No. 730 exposure increased to 2.0 in day 4 at 5
No. 736 exposure increased to 5.0 in day 4 at 5
No. 738 exposure increased to 1.0 in day 4 at 5
No. 739 exposure increased to 2.0 in day 4 at 5
No. 757 exposure increased to 3.0 in day 4 at 5
No. 762 exposure increased to 3.0 in day 4 at 5
No. 769 exposure increased to 2.0 in day 4 at 5
No. 772 exposure increased to 2.0 in day 4 at 5
No. 774 exposure increased to 3.0 in day 4 at 5
No. 776 exposure increased to 1.0 in day 4 at 5
No. 779 exposure increased to 2.0 in day 4 at 5
No. 781 exposure increased to 3.0 in day 4 at 5
No. 785 exposure increased to 1.0 in day 4 at 5
*When No. 786 infected, Exposure is 2.0 in day 4 at move 5
No. 789 exposure increased to 2.0 in day 4 at 5
No. 796 exposure increased to 3.0 in day 4 at 5
No. 802 exposure increased to 2.0 in day 4 at 5
No. 807 exposure increased to 2.0 in day 4 at 5
No. 815 exposure increased to 4.0 in day 4 at 5
No. 816 exposure increased to 1.0 in day 4 at 5
No. 821 exposure increased to 2.0 in day 4 at 5
No. 827 exposure increased to 2.0 in day 4 at 5
No. 828 exposure increased to 2.0 in day 4 at 5
No. 834 exposure increased to 1.0 in day 4 at 5
No. 851 exposure increased to 1.0 in day 4 at 5
No. 852 exposure increased to 1.0 in day 4 at 5
No. 858 exposure increased to 1.0 in day 4 at 5
No. 861 exposure increased to 1.0 in day 4 at 5
No. 862 exposure increased to 3.0 in day 4 at 5
No. 865 exposure increased to 2.0 in day 4 at 5
No. 866 exposure increased to 2.0 in day 4 at 5
No. 869 exposure increased to 2.0 in day 4 at 5
No. 873 exposure increased to 2.0 in day 4 at 5
No. 875 exposure increased to 1.0 in day 4 at 5
No. 877 exposure increased to 2.0 in day 4 at 5
No. 886 exposure increased to 1.0 in day 4 at 5
No. 888 exposure increased to 2.0 in day 4 at 5
No. 889 exposure increased to 1.0 in day 4 at 5
No. 898 exposure increased to 2.0 in day 4 at 5
No. 902 exposure increased to 3.0 in day 4 at 5
No. 912 exposure increased to 2.0 in day 4 at 5
No. 925 exposure increased to 3.0 in day 4 at 5
No. 928 exposure increased to 3.0 in day 4 at 5
No. 930 exposure increased to 3.0 in day 4 at 5
No. 933 exposure increased to 2.0 in day 4 at 5
No. 934 exposure increased to 1.0 in day 4 at 5
No. 935 exposure increased to 1.0 in day 4 at 5
No. 939 exposure increased to 2.0 in day 4 at 5
No. 943 exposure increased to 2.0 in day 4 at 5
No. 948 exposure increased to 2.0 in day 4 at 5
No. 951 exposure increased to 1.0 in day 4 at 5
No. 957 exposure increased to 2.0 in day 4 at 5
No. 958 exposure increased to 2.0 in day 4 at 5
No. 961 exposure increased to 4.0 in day 4 at 5
No. 963 exposure increased to 3.0 in day 4 at 5
No. 964 exposure increased to 2.0 in day 4 at 5
No. 973 exposure increased to 3.0 in day 4 at 5
No. 984 exposure increased to 2.0 in day 4 at 5
No. 998 exposure increased to 3.0 in day 4 at 5
No. 999 exposure increased to 1.0 in day 4 at 5
   27/10000 [..............................] - ETA: 31:55:33 - reward: 812.2296*When No. 130 infected, Exposure is 2.0 in day 4 at move 0
*When No. 227 infected, Exposure is 2.0 in day 4 at move 0
*When No. 244 infected, Exposure is 4.0 in day 4 at move 0
*When No. 271 infected, Exposure is 3.0 in day 4 at move 0
*When No. 302 infected, Exposure is 3.0 in day 4 at move 0
*When No. 364 infected, Exposure is 2.0 in day 4 at move 0
*When No. 481 infected, Exposure is 2.0 in day 4 at move 0
*When No. 739 infected, Exposure is 2.0 in day 4 at move 0
*When No. 802 infected, Exposure is 2.0 in day 4 at move 0
*When No. 815 infected, Exposure is 4.0 in day 4 at move 0
*When No. 957 infected, Exposure is 2.0 in day 4 at move 0
No. 2 exposure increased to 3.0 in day 4 at 1
No. 4 exposure increased to 3.0 in day 4 at 1
No. 7 exposure increased to 4.0 in day 4 at 1
No. 17 exposure increased to 4.0 in day 4 at 1
No. 20 exposure increased to 3.0 in day 4 at 1
No. 24 exposure increased to 1.0 in day 4 at 1
No. 27 exposure increased to 3.0 in day 4 at 1
No. 33 exposure increased to 2.0 in day 4 at 1
No. 38 exposure increased to 6.0 in day 4 at 1
No. 40 exposure increased to 2.0 in day 4 at 1
No. 41 exposure increased to 2.0 in day 4 at 1
No. 63 exposure increased to 2.0 in day 4 at 1
No. 73 exposure increased to 3.0 in day 4 at 1
No. 79 exposure increased to 3.0 in day 4 at 1
No. 84 exposure increased to 3.0 in day 4 at 1
No. 89 exposure increased to 1.0 in day 4 at 1
No. 93 exposure increased to 2.0 in day 4 at 1
No. 104 exposure increased to 3.0 in day 4 at 1
No. 109 exposure increased to 2.0 in day 4 at 1
No. 115 exposure increased to 3.0 in day 4 at 1
No. 116 exposure increased to 3.0 in day 4 at 1
No. 117 exposure increased to 3.0 in day 4 at 1
No. 132 exposure increased to 2.0 in day 4 at 1
No. 133 exposure increased to 2.0 in day 4 at 1
No. 147 exposure increased to 4.0 in day 4 at 1
No. 151 exposure increased to 2.0 in day 4 at 1
No. 154 exposure increased to 4.0 in day 4 at 1
No. 156 exposure increased to 3.0 in day 4 at 1
No. 175 exposure increased to 5.0 in day 4 at 1
No. 179 exposure increased to 2.0 in day 4 at 1
No. 197 exposure increased to 3.0 in day 4 at 1
No. 198 exposure increased to 2.0 in day 4 at 1
No. 199 exposure increased to 4.0 in day 4 at 1
No. 200 exposure increased to 1.0 in day 4 at 1
No. 203 exposure increased to 3.0 in day 4 at 1
No. 214 exposure increased to 3.0 in day 4 at 1
*When No. 217 infected, Exposure is 2.0 in day 4 at move 1
No. 220 exposure increased to 1.0 in day 4 at 1
No. 233 exposure increased to 2.0 in day 4 at 1
No. 241 exposure increased to 2.0 in day 4 at 1
No. 245 exposure increased to 2.0 in day 4 at 1
No. 265 exposure increased to 2.0 in day 4 at 1
No. 266 exposure increased to 2.0 in day 4 at 1
No. 267 exposure increased to 1.0 in day 4 at 1
No. 268 exposure increased to 2.0 in day 4 at 1
No. 269 exposure increased to 4.0 in day 4 at 1
No. 281 exposure increased to 2.0 in day 4 at 1
No. 284 exposure increased to 2.0 in day 4 at 1
No. 294 exposure increased to 2.0 in day 4 at 1
No. 295 exposure increased to 3.0 in day 4 at 1
No. 296 exposure increased to 3.0 in day 4 at 1
No. 297 exposure increased to 2.0 in day 4 at 1
No. 310 exposure increased to 3.0 in day 4 at 1
No. 311 exposure increased to 3.0 in day 4 at 1
No. 316 exposure increased to 3.0 in day 4 at 1
No. 325 exposure increased to 3.0 in day 4 at 1
No. 329 exposure increased to 5.0 in day 4 at 1
No. 359 exposure increased to 3.0 in day 4 at 1
No. 361 exposure increased to 4.0 in day 4 at 1
No. 362 exposure increased to 1.0 in day 4 at 1
No. 389 exposure increased to 2.0 in day 4 at 1
*When No. 394 infected, Exposure is 2.0 in day 4 at move 1
No. 395 exposure increased to 2.0 in day 4 at 1
No. 396 exposure increased to 3.0 in day 4 at 1
No. 405 exposure increased to 3.0 in day 4 at 1
No. 420 exposure increased to 2.0 in day 4 at 1
*When No. 427 infected, Exposure is 3.0 in day 4 at move 1
No. 436 exposure increased to 2.0 in day 4 at 1
No. 441 exposure increased to 2.0 in day 4 at 1
No. 447 exposure increased to 5.0 in day 4 at 1
No. 459 exposure increased to 2.0 in day 4 at 1
*When No. 464 infected, Exposure is 3.0 in day 4 at move 1
No. 473 exposure increased to 3.0 in day 4 at 1
No. 476 exposure increased to 3.0 in day 4 at 1
No. 482 exposure increased to 2.0 in day 4 at 1
No. 485 exposure increased to 3.0 in day 4 at 1
No. 489 exposure increased to 3.0 in day 4 at 1
No. 507 exposure increased to 1.0 in day 4 at 1
*When No. 512 infected, Exposure is 3.0 in day 4 at move 1
No. 513 exposure increased to 3.0 in day 4 at 1
No. 518 exposure increased to 2.0 in day 4 at 1
No. 526 exposure increased to 2.0 in day 4 at 1
No. 529 exposure increased to 2.0 in day 4 at 1
No. 535 exposure increased to 2.0 in day 4 at 1
*When No. 545 infected, Exposure is 2.0 in day 4 at move 1
No. 546 exposure increased to 4.0 in day 4 at 1
No. 551 exposure increased to 2.0 in day 4 at 1
No. 559 exposure increased to 4.0 in day 4 at 1
No. 567 exposure increased to 2.0 in day 4 at 1
No. 568 exposure increased to 3.0 in day 4 at 1
No. 569 exposure increased to 2.0 in day 4 at 1
No. 577 exposure increased to 3.0 in day 4 at 1
No. 580 exposure increased to 3.0 in day 4 at 1
*When No. 583 infected, Exposure is 4.0 in day 4 at move 1
No. 587 exposure increased to 2.0 in day 4 at 1
No. 598 exposure increased to 3.0 in day 4 at 1
No. 600 exposure increased to 3.0 in day 4 at 1
No. 604 exposure increased to 3.0 in day 4 at 1
No. 605 exposure increased to 2.0 in day 4 at 1
No. 616 exposure increased to 3.0 in day 4 at 1
No. 619 exposure increased to 2.0 in day 4 at 1
No. 624 exposure increased to 1.0 in day 4 at 1
*When No. 630 infected, Exposure is 2.0 in day 4 at move 1
No. 633 exposure increased to 1.0 in day 4 at 1
No. 641 exposure increased to 2.0 in day 4 at 1
*When No. 642 infected, Exposure is 2.0 in day 4 at move 1
No. 645 exposure increased to 5.0 in day 4 at 1
No. 655 exposure increased to 2.0 in day 4 at 1
*When No. 667 infected, Exposure is 3.0 in day 4 at move 1
*When No. 669 infected, Exposure is 2.0 in day 4 at move 1
No. 673 exposure increased to 2.0 in day 4 at 1
No. 677 exposure increased to 1.0 in day 4 at 1
No. 678 exposure increased to 3.0 in day 4 at 1
No. 680 exposure increased to 2.0 in day 4 at 1
No. 682 exposure increased to 3.0 in day 4 at 1
No. 685 exposure increased to 3.0 in day 4 at 1
No. 691 exposure increased to 2.0 in day 4 at 1
No. 703 exposure increased to 3.0 in day 4 at 1
No. 710 exposure increased to 2.0 in day 4 at 1
No. 712 exposure increased to 2.0 in day 4 at 1
No. 730 exposure increased to 3.0 in day 4 at 1
No. 731 exposure increased to 2.0 in day 4 at 1
*When No. 736 infected, Exposure is 5.0 in day 4 at move 1
No. 738 exposure increased to 2.0 in day 4 at 1
No. 746 exposure increased to 2.0 in day 4 at 1
No. 757 exposure increased to 4.0 in day 4 at 1
No. 762 exposure increased to 4.0 in day 4 at 1
No. 769 exposure increased to 3.0 in day 4 at 1
No. 772 exposure increased to 3.0 in day 4 at 1
No. 774 exposure increased to 4.0 in day 4 at 1
No. 776 exposure increased to 2.0 in day 4 at 1
*When No. 779 infected, Exposure is 2.0 in day 4 at move 1
No. 781 exposure increased to 4.0 in day 4 at 1
No. 785 exposure increased to 2.0 in day 4 at 1
No. 789 exposure increased to 3.0 in day 4 at 1
*When No. 796 infected, Exposure is 3.0 in day 4 at move 1
No. 803 exposure increased to 1.0 in day 4 at 1
No. 807 exposure increased to 3.0 in day 4 at 1
No. 816 exposure increased to 2.0 in day 4 at 1
No. 821 exposure increased to 3.0 in day 4 at 1
No. 827 exposure increased to 3.0 in day 4 at 1
No. 828 exposure increased to 3.0 in day 4 at 1
No. 834 exposure increased to 2.0 in day 4 at 1
No. 851 exposure increased to 2.0 in day 4 at 1
No. 852 exposure increased to 2.0 in day 4 at 1
No. 856 exposure increased to 2.0 in day 4 at 1
No. 858 exposure increased to 2.0 in day 4 at 1
No. 861 exposure increased to 2.0 in day 4 at 1
No. 862 exposure increased to 4.0 in day 4 at 1
No. 865 exposure increased to 3.0 in day 4 at 1
No. 866 exposure increased to 3.0 in day 4 at 1
No. 869 exposure increased to 3.0 in day 4 at 1
No. 873 exposure increased to 3.0 in day 4 at 1
No. 875 exposure increased to 2.0 in day 4 at 1
No. 877 exposure increased to 3.0 in day 4 at 1
No. 886 exposure increased to 2.0 in day 4 at 1
No. 888 exposure increased to 3.0 in day 4 at 1
No. 889 exposure increased to 2.0 in day 4 at 1
No. 898 exposure increased to 3.0 in day 4 at 1
No. 902 exposure increased to 4.0 in day 4 at 1
No. 908 exposure increased to 1.0 in day 4 at 1
*When No. 912 infected, Exposure is 2.0 in day 4 at move 1
No. 925 exposure increased to 4.0 in day 4 at 1
No. 928 exposure increased to 4.0 in day 4 at 1
*When No. 930 infected, Exposure is 3.0 in day 4 at move 1
No. 933 exposure increased to 3.0 in day 4 at 1
No. 934 exposure increased to 2.0 in day 4 at 1
No. 935 exposure increased to 2.0 in day 4 at 1
No. 939 exposure increased to 3.0 in day 4 at 1
No. 943 exposure increased to 3.0 in day 4 at 1
No. 948 exposure increased to 3.0 in day 4 at 1
No. 951 exposure increased to 2.0 in day 4 at 1
No. 958 exposure increased to 3.0 in day 4 at 1
*When No. 961 infected, Exposure is 4.0 in day 4 at move 1
No. 963 exposure increased to 4.0 in day 4 at 1
No. 964 exposure increased to 3.0 in day 4 at 1
*When No. 973 infected, Exposure is 3.0 in day 4 at move 1
No. 984 exposure increased to 3.0 in day 4 at 1
No. 998 exposure increased to 4.0 in day 4 at 1
No. 999 exposure increased to 2.0 in day 4 at 1
   28/10000 [..............................] - ETA: 31:09:48 - reward: 800.1243*When No. 7 infected, Exposure is 4.0 in day 4 at move 0
*When No. 20 infected, Exposure is 3.0 in day 4 at move 0
*When No. 38 infected, Exposure is 6.0 in day 4 at move 0
*When No. 79 infected, Exposure is 3.0 in day 4 at move 0
*When No. 245 infected, Exposure is 2.0 in day 4 at move 0
*When No. 310 infected, Exposure is 3.0 in day 4 at move 0
*When No. 311 infected, Exposure is 3.0 in day 4 at move 0
*When No. 316 infected, Exposure is 3.0 in day 4 at move 0
*When No. 489 infected, Exposure is 3.0 in day 4 at move 0
*When No. 518 infected, Exposure is 2.0 in day 4 at move 0
*When No. 529 infected, Exposure is 2.0 in day 4 at move 0
*When No. 546 infected, Exposure is 4.0 in day 4 at move 0
*When No. 645 infected, Exposure is 5.0 in day 4 at move 0
*When No. 685 infected, Exposure is 3.0 in day 4 at move 0
*When No. 757 infected, Exposure is 4.0 in day 4 at move 0
*When No. 762 infected, Exposure is 4.0 in day 4 at move 0
*When No. 781 infected, Exposure is 4.0 in day 4 at move 0
*When No. 816 infected, Exposure is 2.0 in day 4 at move 0
*When No. 865 infected, Exposure is 3.0 in day 4 at move 0
*When No. 898 infected, Exposure is 3.0 in day 4 at move 0
*When No. 902 infected, Exposure is 4.0 in day 4 at move 0
*When No. 925 infected, Exposure is 4.0 in day 4 at move 0
*When No. 928 infected, Exposure is 4.0 in day 4 at move 0
*When No. 999 infected, Exposure is 2.0 in day 4 at move 0
*When No. 2 infected, Exposure is 3.0 in day 4 at move 1
*When No. 4 infected, Exposure is 3.0 in day 4 at move 1
*When No. 27 infected, Exposure is 3.0 in day 4 at move 1
*When No. 104 infected, Exposure is 3.0 in day 4 at move 1
*When No. 154 infected, Exposure is 4.0 in day 4 at move 1
*When No. 396 infected, Exposure is 3.0 in day 4 at move 1
*When No. 447 infected, Exposure is 5.0 in day 4 at move 1
*When No. 513 infected, Exposure is 3.0 in day 4 at move 1
*When No. 551 infected, Exposure is 2.0 in day 4 at move 1
*When No. 678 infected, Exposure is 3.0 in day 4 at move 1
*When No. 682 infected, Exposure is 3.0 in day 4 at move 1
*When No. 703 infected, Exposure is 3.0 in day 4 at move 1
*When No. 712 infected, Exposure is 2.0 in day 4 at move 1
*When No. 730 infected, Exposure is 3.0 in day 4 at move 1
*When No. 774 infected, Exposure is 4.0 in day 4 at move 1
*When No. 888 infected, Exposure is 3.0 in day 4 at move 1
*When No. 939 infected, Exposure is 3.0 in day 4 at move 1
*When No. 84 infected, Exposure is 3.0 in day 4 at move 2
*When No. 115 infected, Exposure is 3.0 in day 4 at move 2
*When No. 117 infected, Exposure is 3.0 in day 4 at move 2
*When No. 132 infected, Exposure is 2.0 in day 4 at move 2
*When No. 151 infected, Exposure is 2.0 in day 4 at move 2
*When No. 197 infected, Exposure is 3.0 in day 4 at move 2
*When No. 203 infected, Exposure is 3.0 in day 4 at move 2
*When No. 214 infected, Exposure is 3.0 in day 4 at move 2
*When No. 265 infected, Exposure is 2.0 in day 4 at move 2
*When No. 297 infected, Exposure is 2.0 in day 4 at move 2
*When No. 325 infected, Exposure is 3.0 in day 4 at move 2
*When No. 395 infected, Exposure is 2.0 in day 4 at move 2
*When No. 476 infected, Exposure is 3.0 in day 4 at move 2
*When No. 482 infected, Exposure is 2.0 in day 4 at move 2
*When No. 485 infected, Exposure is 3.0 in day 4 at move 2
*When No. 587 infected, Exposure is 2.0 in day 4 at move 2
*When No. 600 infected, Exposure is 3.0 in day 4 at move 2
*When No. 769 infected, Exposure is 3.0 in day 4 at move 2
*When No. 807 infected, Exposure is 3.0 in day 4 at move 2
*When No. 866 infected, Exposure is 3.0 in day 4 at move 2
*When No. 933 infected, Exposure is 3.0 in day 4 at move 2
*When No. 948 infected, Exposure is 3.0 in day 4 at move 2
*When No. 175 infected, Exposure is 5.0 in day 4 at move 3
*When No. 199 infected, Exposure is 4.0 in day 4 at move 3
*When No. 284 infected, Exposure is 2.0 in day 4 at move 3
*When No. 294 infected, Exposure is 2.0 in day 4 at move 3
*When No. 296 infected, Exposure is 3.0 in day 4 at move 3
*When No. 329 infected, Exposure is 5.0 in day 4 at move 3
*When No. 361 infected, Exposure is 4.0 in day 4 at move 3
*When No. 776 infected, Exposure is 2.0 in day 4 at move 3
*When No. 951 infected, Exposure is 2.0 in day 4 at move 3
*When No. 17 infected, Exposure is 4.0 in day 4 at move 4
*When No. 40 infected, Exposure is 2.0 in day 4 at move 4
*When No. 41 infected, Exposure is 2.0 in day 4 at move 4
*When No. 268 infected, Exposure is 2.0 in day 4 at move 4
*When No. 295 infected, Exposure is 3.0 in day 4 at move 4
*When No. 359 infected, Exposure is 3.0 in day 4 at move 4
*When No. 420 infected, Exposure is 2.0 in day 4 at move 4
*When No. 559 infected, Exposure is 4.0 in day 4 at move 4
*When No. 568 infected, Exposure is 3.0 in day 4 at move 4
*When No. 577 infected, Exposure is 3.0 in day 4 at move 4
*When No. 604 infected, Exposure is 3.0 in day 4 at move 4
*When No. 827 infected, Exposure is 3.0 in day 4 at move 4
*When No. 861 infected, Exposure is 2.0 in day 4 at move 4
*When No. 875 infected, Exposure is 2.0 in day 4 at move 4
*When No. 877 infected, Exposure is 3.0 in day 4 at move 4
*When No. 943 infected, Exposure is 3.0 in day 4 at move 4
*When No. 984 infected, Exposure is 3.0 in day 4 at move 4
No. 10 exposure increased to 1.0 in day 4 at 5
No. 18 exposure increased to 2.0 in day 4 at 5
No. 24 exposure increased to 2.0 in day 4 at 5
No. 33 exposure increased to 3.0 in day 4 at 5
No. 37 exposure increased to 2.0 in day 4 at 5
No. 63 exposure increased to 3.0 in day 4 at 5
No. 73 exposure increased to 4.0 in day 4 at 5
No. 83 exposure increased to 1.0 in day 4 at 5
No. 89 exposure increased to 2.0 in day 4 at 5
*When No. 93 infected, Exposure is 2.0 in day 4 at move 5
No. 95 exposure increased to 1.0 in day 4 at 5
No. 106 exposure increased to 1.0 in day 4 at 5
No. 109 exposure increased to 3.0 in day 4 at 5
No. 116 exposure increased to 4.0 in day 4 at 5
No. 119 exposure increased to 1.0 in day 4 at 5
No. 133 exposure increased to 3.0 in day 4 at 5
No. 135 exposure increased to 1.0 in day 4 at 5
No. 147 exposure increased to 5.0 in day 4 at 5
No. 156 exposure increased to 4.0 in day 4 at 5
No. 173 exposure increased to 1.0 in day 4 at 5
*When No. 179 infected, Exposure is 2.0 in day 4 at move 5
No. 183 exposure increased to 1.0 in day 4 at 5
*When No. 198 infected, Exposure is 2.0 in day 4 at move 5
No. 200 exposure increased to 2.0 in day 4 at 5
No. 204 exposure increased to 1.0 in day 4 at 5
No. 220 exposure increased to 2.0 in day 4 at 5
*When No. 233 infected, Exposure is 2.0 in day 4 at move 5
No. 241 exposure increased to 3.0 in day 4 at 5
No. 266 exposure increased to 3.0 in day 4 at 5
No. 267 exposure increased to 2.0 in day 4 at 5
No. 269 exposure increased to 5.0 in day 4 at 5
No. 274 exposure increased to 1.0 in day 4 at 5
No. 281 exposure increased to 3.0 in day 4 at 5
No. 291 exposure increased to 1.0 in day 4 at 5
No. 339 exposure increased to 1.0 in day 4 at 5
No. 340 exposure increased to 1.0 in day 4 at 5
No. 341 exposure increased to 2.0 in day 4 at 5
No. 343 exposure increased to 1.0 in day 4 at 5
No. 362 exposure increased to 2.0 in day 4 at 5
No. 379 exposure increased to 1.0 in day 4 at 5
No. 387 exposure increased to 1.0 in day 4 at 5
No. 389 exposure increased to 3.0 in day 4 at 5
No. 405 exposure increased to 4.0 in day 4 at 5
No. 436 exposure increased to 3.0 in day 4 at 5
No. 441 exposure increased to 3.0 in day 4 at 5
No. 446 exposure increased to 1.0 in day 4 at 5
No. 448 exposure increased to 1.0 in day 4 at 5
No. 459 exposure increased to 3.0 in day 4 at 5
No. 473 exposure increased to 4.0 in day 4 at 5
No. 507 exposure increased to 2.0 in day 4 at 5
No. 514 exposure increased to 1.0 in day 4 at 5
No. 520 exposure increased to 1.0 in day 4 at 5
No. 526 exposure increased to 3.0 in day 4 at 5
No. 535 exposure increased to 3.0 in day 4 at 5
No. 537 exposure increased to 2.0 in day 4 at 5
No. 560 exposure increased to 2.0 in day 4 at 5
No. 567 exposure increased to 3.0 in day 4 at 5
No. 569 exposure increased to 3.0 in day 4 at 5
No. 575 exposure increased to 1.0 in day 4 at 5
No. 580 exposure increased to 4.0 in day 4 at 5
No. 581 exposure increased to 1.0 in day 4 at 5
No. 584 exposure increased to 2.0 in day 4 at 5
No. 590 exposure increased to 1.0 in day 4 at 5
*When No. 598 infected, Exposure is 3.0 in day 4 at move 5
No. 605 exposure increased to 3.0 in day 4 at 5
No. 616 exposure increased to 4.0 in day 4 at 5
No. 619 exposure increased to 3.0 in day 4 at 5
No. 624 exposure increased to 2.0 in day 4 at 5
No. 633 exposure increased to 2.0 in day 4 at 5
No. 641 exposure increased to 3.0 in day 4 at 5
No. 655 exposure increased to 3.0 in day 4 at 5
No. 672 exposure increased to 2.0 in day 4 at 5
No. 673 exposure increased to 3.0 in day 4 at 5
No. 677 exposure increased to 2.0 in day 4 at 5
No. 680 exposure increased to 3.0 in day 4 at 5
No. 686 exposure increased to 2.0 in day 4 at 5
No. 691 exposure increased to 3.0 in day 4 at 5
No. 694 exposure increased to 1.0 in day 4 at 5
No. 696 exposure increased to 1.0 in day 4 at 5
No. 710 exposure increased to 3.0 in day 4 at 5
No. 711 exposure increased to 1.0 in day 4 at 5
No. 731 exposure increased to 3.0 in day 4 at 5
No. 738 exposure increased to 3.0 in day 4 at 5
No. 746 exposure increased to 3.0 in day 4 at 5
No. 772 exposure increased to 4.0 in day 4 at 5
No. 784 exposure increased to 1.0 in day 4 at 5
No. 785 exposure increased to 3.0 in day 4 at 5
No. 789 exposure increased to 4.0 in day 4 at 5
No. 803 exposure increased to 2.0 in day 4 at 5
No. 821 exposure increased to 4.0 in day 4 at 5
*When No. 828 infected, Exposure is 3.0 in day 4 at move 5
No. 830 exposure increased to 1.0 in day 4 at 5
No. 834 exposure increased to 3.0 in day 4 at 5
No. 839 exposure increased to 1.0 in day 4 at 5
No. 842 exposure increased to 1.0 in day 4 at 5
No. 851 exposure increased to 3.0 in day 4 at 5
No. 852 exposure increased to 3.0 in day 4 at 5
No. 856 exposure increased to 3.0 in day 4 at 5
No. 858 exposure increased to 3.0 in day 4 at 5
*When No. 862 infected, Exposure is 4.0 in day 4 at move 5
No. 869 exposure increased to 4.0 in day 4 at 5
No. 873 exposure increased to 4.0 in day 4 at 5
No. 886 exposure increased to 3.0 in day 4 at 5
No. 889 exposure increased to 3.0 in day 4 at 5
No. 895 exposure increased to 1.0 in day 4 at 5
No. 899 exposure increased to 1.0 in day 4 at 5
No. 907 exposure increased to 2.0 in day 4 at 5
No. 908 exposure increased to 2.0 in day 4 at 5
No. 917 exposure increased to 2.0 in day 4 at 5
No. 934 exposure increased to 3.0 in day 4 at 5
No. 935 exposure increased to 3.0 in day 4 at 5
No. 958 exposure increased to 4.0 in day 4 at 5
No. 963 exposure increased to 5.0 in day 4 at 5
No. 964 exposure increased to 4.0 in day 4 at 5
No. 975 exposure increased to 1.0 in day 4 at 5
No. 989 exposure increased to 1.0 in day 4 at 5
*When No. 998 infected, Exposure is 4.0 in day 4 at move 5
   29/10000 [..............................] - ETA: 31:10:27 - reward: 787.3641*When No. 73 infected, Exposure is 4.0 in day 4 at move 0
*When No. 116 infected, Exposure is 4.0 in day 4 at move 0
*When No. 156 infected, Exposure is 4.0 in day 4 at move 0
*When No. 266 infected, Exposure is 3.0 in day 4 at move 0
*When No. 441 infected, Exposure is 3.0 in day 4 at move 0
*When No. 655 infected, Exposure is 3.0 in day 4 at move 0
*When No. 680 infected, Exposure is 3.0 in day 4 at move 0
*When No. 710 infected, Exposure is 3.0 in day 4 at move 0
*When No. 731 infected, Exposure is 3.0 in day 4 at move 0
*When No. 803 infected, Exposure is 2.0 in day 4 at move 0
*When No. 869 infected, Exposure is 4.0 in day 4 at move 0
*When No. 907 infected, Exposure is 2.0 in day 4 at move 0
*When No. 958 infected, Exposure is 4.0 in day 4 at move 0
No. 10 exposure increased to 2.0 in day 4 at 1
No. 18 exposure increased to 3.0 in day 4 at 1
*When No. 24 infected, Exposure is 2.0 in day 4 at move 1
No. 33 exposure increased to 4.0 in day 4 at 1
No. 37 exposure increased to 3.0 in day 4 at 1
No. 63 exposure increased to 4.0 in day 4 at 1
No. 76 exposure increased to 2.0 in day 4 at 1
No. 81 exposure increased to 2.0 in day 4 at 1
No. 83 exposure increased to 2.0 in day 4 at 1
No. 89 exposure increased to 3.0 in day 4 at 1
No. 94 exposure increased to 2.0 in day 4 at 1
No. 95 exposure increased to 2.0 in day 4 at 1
No. 106 exposure increased to 2.0 in day 4 at 1
No. 109 exposure increased to 4.0 in day 4 at 1
No. 119 exposure increased to 2.0 in day 4 at 1
No. 133 exposure increased to 4.0 in day 4 at 1
No. 135 exposure increased to 2.0 in day 4 at 1
No. 143 exposure increased to 2.0 in day 4 at 1
No. 147 exposure increased to 6.0 in day 4 at 1
No. 173 exposure increased to 2.0 in day 4 at 1
No. 183 exposure increased to 2.0 in day 4 at 1
No. 200 exposure increased to 3.0 in day 4 at 1
No. 201 exposure increased to 1.0 in day 4 at 1
No. 204 exposure increased to 2.0 in day 4 at 1
No. 206 exposure increased to 2.0 in day 4 at 1
*When No. 220 infected, Exposure is 2.0 in day 4 at move 1
No. 238 exposure increased to 1.0 in day 4 at 1
No. 241 exposure increased to 4.0 in day 4 at 1
No. 260 exposure increased to 1.0 in day 4 at 1
No. 267 exposure increased to 3.0 in day 4 at 1
*When No. 269 infected, Exposure is 5.0 in day 4 at move 1
No. 274 exposure increased to 2.0 in day 4 at 1
*When No. 281 infected, Exposure is 3.0 in day 4 at move 1
No. 291 exposure increased to 2.0 in day 4 at 1
No. 301 exposure increased to 2.0 in day 4 at 1
No. 339 exposure increased to 2.0 in day 4 at 1
No. 340 exposure increased to 2.0 in day 4 at 1
No. 341 exposure increased to 3.0 in day 4 at 1
No. 343 exposure increased to 2.0 in day 4 at 1
No. 362 exposure increased to 3.0 in day 4 at 1
No. 379 exposure increased to 2.0 in day 4 at 1
No. 387 exposure increased to 2.0 in day 4 at 1
No. 389 exposure increased to 4.0 in day 4 at 1
No. 405 exposure increased to 5.0 in day 4 at 1
No. 435 exposure increased to 2.0 in day 4 at 1
No. 436 exposure increased to 4.0 in day 4 at 1
No. 446 exposure increased to 2.0 in day 4 at 1
No. 448 exposure increased to 2.0 in day 4 at 1
No. 459 exposure increased to 4.0 in day 4 at 1
No. 461 exposure increased to 1.0 in day 4 at 1
No. 469 exposure increased to 1.0 in day 4 at 1
No. 473 exposure increased to 5.0 in day 4 at 1
No. 474 exposure increased to 2.0 in day 4 at 1
No. 483 exposure increased to 1.0 in day 4 at 1
No. 507 exposure increased to 3.0 in day 4 at 1
No. 514 exposure increased to 2.0 in day 4 at 1
No. 520 exposure increased to 2.0 in day 4 at 1
No. 526 exposure increased to 4.0 in day 4 at 1
No. 535 exposure increased to 4.0 in day 4 at 1
No. 537 exposure increased to 3.0 in day 4 at 1
No. 560 exposure increased to 3.0 in day 4 at 1
*When No. 567 infected, Exposure is 3.0 in day 4 at move 1
No. 569 exposure increased to 4.0 in day 4 at 1
No. 575 exposure increased to 2.0 in day 4 at 1
No. 580 exposure increased to 5.0 in day 4 at 1
No. 581 exposure increased to 2.0 in day 4 at 1
No. 584 exposure increased to 3.0 in day 4 at 1
No. 590 exposure increased to 2.0 in day 4 at 1
No. 605 exposure increased to 4.0 in day 4 at 1
No. 611 exposure increased to 2.0 in day 4 at 1
No. 614 exposure increased to 1.0 in day 4 at 1
*When No. 616 infected, Exposure is 4.0 in day 4 at move 1
No. 619 exposure increased to 4.0 in day 4 at 1
No. 624 exposure increased to 3.0 in day 4 at 1
No. 633 exposure increased to 3.0 in day 4 at 1
No. 641 exposure increased to 4.0 in day 4 at 1
No. 672 exposure increased to 3.0 in day 4 at 1
*When No. 673 infected, Exposure is 3.0 in day 4 at move 1
No. 677 exposure increased to 3.0 in day 4 at 1
No. 686 exposure increased to 3.0 in day 4 at 1
No. 691 exposure increased to 4.0 in day 4 at 1
No. 694 exposure increased to 2.0 in day 4 at 1
No. 696 exposure increased to 2.0 in day 4 at 1
No. 706 exposure increased to 2.0 in day 4 at 1
No. 711 exposure increased to 2.0 in day 4 at 1
No. 735 exposure increased to 1.0 in day 4 at 1
*When No. 738 infected, Exposure is 3.0 in day 4 at move 1
No. 740 exposure increased to 2.0 in day 4 at 1
No. 746 exposure increased to 4.0 in day 4 at 1
*When No. 772 infected, Exposure is 4.0 in day 4 at move 1
No. 784 exposure increased to 2.0 in day 4 at 1
No. 785 exposure increased to 4.0 in day 4 at 1
No. 789 exposure increased to 5.0 in day 4 at 1
*When No. 821 infected, Exposure is 4.0 in day 4 at move 1
No. 830 exposure increased to 2.0 in day 4 at 1
No. 832 exposure increased to 1.0 in day 4 at 1
No. 833 exposure increased to 2.0 in day 4 at 1
No. 834 exposure increased to 4.0 in day 4 at 1
No. 839 exposure increased to 2.0 in day 4 at 1
No. 842 exposure increased to 2.0 in day 4 at 1
No. 851 exposure increased to 4.0 in day 4 at 1
No. 852 exposure increased to 4.0 in day 4 at 1
No. 856 exposure increased to 4.0 in day 4 at 1
No. 858 exposure increased to 4.0 in day 4 at 1
*When No. 873 infected, Exposure is 4.0 in day 4 at move 1
No. 886 exposure increased to 4.0 in day 4 at 1
No. 889 exposure increased to 4.0 in day 4 at 1
No. 895 exposure increased to 2.0 in day 4 at 1
No. 899 exposure increased to 2.0 in day 4 at 1
No. 904 exposure increased to 2.0 in day 4 at 1
No. 908 exposure increased to 3.0 in day 4 at 1
No. 917 exposure increased to 3.0 in day 4 at 1
No. 934 exposure increased to 4.0 in day 4 at 1
No. 935 exposure increased to 4.0 in day 4 at 1
No. 962 exposure increased to 2.0 in day 4 at 1
No. 963 exposure increased to 6.0 in day 4 at 1
No. 964 exposure increased to 5.0 in day 4 at 1
No. 965 exposure increased to 2.0 in day 4 at 1
No. 969 exposure increased to 1.0 in day 4 at 1
No. 975 exposure increased to 2.0 in day 4 at 1
No. 989 exposure increased to 2.0 in day 4 at 1
   30/10000 [..............................] - ETA: 30:28:22 - reward: 775.0020*When No. 10 infected, Exposure is 2.0 in day 4 at move 0
*When No. 18 infected, Exposure is 3.0 in day 4 at move 0
*When No. 33 infected, Exposure is 4.0 in day 4 at move 0
*When No. 63 infected, Exposure is 4.0 in day 4 at move 0
*When No. 119 infected, Exposure is 2.0 in day 4 at move 0
*When No. 133 infected, Exposure is 4.0 in day 4 at move 0
*When No. 147 infected, Exposure is 6.0 in day 4 at move 0
*When No. 206 infected, Exposure is 2.0 in day 4 at move 0
*When No. 339 infected, Exposure is 2.0 in day 4 at move 0
*When No. 436 infected, Exposure is 4.0 in day 4 at move 0
*When No. 473 infected, Exposure is 5.0 in day 4 at move 0
*When No. 507 infected, Exposure is 3.0 in day 4 at move 0
*When No. 580 infected, Exposure is 5.0 in day 4 at move 0
*When No. 633 infected, Exposure is 3.0 in day 4 at move 0
*When No. 691 infected, Exposure is 4.0 in day 4 at move 0
*When No. 886 infected, Exposure is 4.0 in day 4 at move 0
*When No. 934 infected, Exposure is 4.0 in day 4 at move 0
*When No. 935 infected, Exposure is 4.0 in day 4 at move 0
*When No. 989 infected, Exposure is 2.0 in day 4 at move 0
No. 0 exposure increased to 1.0 in day 4 at 1
*When No. 37 infected, Exposure is 3.0 in day 4 at move 1
No. 76 exposure increased to 3.0 in day 4 at 1
No. 81 exposure increased to 3.0 in day 4 at 1
No. 83 exposure increased to 3.0 in day 4 at 1
No. 89 exposure increased to 4.0 in day 4 at 1
No. 91 exposure increased to 1.0 in day 4 at 1
No. 94 exposure increased to 3.0 in day 4 at 1
No. 95 exposure increased to 3.0 in day 4 at 1
No. 106 exposure increased to 3.0 in day 4 at 1
No. 109 exposure increased to 5.0 in day 4 at 1
No. 112 exposure increased to 2.0 in day 4 at 1
No. 135 exposure increased to 3.0 in day 4 at 1
No. 143 exposure increased to 3.0 in day 4 at 1
No. 167 exposure increased to 2.0 in day 4 at 1
No. 173 exposure increased to 3.0 in day 4 at 1
No. 183 exposure increased to 3.0 in day 4 at 1
No. 191 exposure increased to 2.0 in day 4 at 1
No. 193 exposure increased to 1.0 in day 4 at 1
No. 200 exposure increased to 4.0 in day 4 at 1
No. 201 exposure increased to 2.0 in day 4 at 1
No. 204 exposure increased to 3.0 in day 4 at 1
No. 234 exposure increased to 1.0 in day 4 at 1
No. 238 exposure increased to 2.0 in day 4 at 1
No. 241 exposure increased to 5.0 in day 4 at 1
No. 260 exposure increased to 2.0 in day 4 at 1
No. 267 exposure increased to 4.0 in day 4 at 1
No. 274 exposure increased to 3.0 in day 4 at 1
No. 277 exposure increased to 1.0 in day 4 at 1
No. 291 exposure increased to 3.0 in day 4 at 1
No. 301 exposure increased to 3.0 in day 4 at 1
No. 317 exposure increased to 1.0 in day 4 at 1
No. 331 exposure increased to 2.0 in day 4 at 1
No. 340 exposure increased to 3.0 in day 4 at 1
No. 341 exposure increased to 4.0 in day 4 at 1
No. 343 exposure increased to 3.0 in day 4 at 1
No. 350 exposure increased to 1.0 in day 4 at 1
No. 355 exposure increased to 2.0 in day 4 at 1
No. 362 exposure increased to 4.0 in day 4 at 1
No. 379 exposure increased to 3.0 in day 4 at 1
No. 387 exposure increased to 3.0 in day 4 at 1
No. 389 exposure increased to 5.0 in day 4 at 1
No. 397 exposure increased to 2.0 in day 4 at 1
*When No. 405 infected, Exposure is 5.0 in day 4 at move 1
No. 434 exposure increased to 2.0 in day 4 at 1
No. 435 exposure increased to 3.0 in day 4 at 1
No. 446 exposure increased to 3.0 in day 4 at 1
No. 448 exposure increased to 3.0 in day 4 at 1
No. 458 exposure increased to 1.0 in day 4 at 1
*When No. 459 infected, Exposure is 4.0 in day 4 at move 1
No. 461 exposure increased to 2.0 in day 4 at 1
No. 469 exposure increased to 2.0 in day 4 at 1
No. 474 exposure increased to 3.0 in day 4 at 1
No. 483 exposure increased to 2.0 in day 4 at 1
No. 505 exposure increased to 1.0 in day 4 at 1
No. 514 exposure increased to 3.0 in day 4 at 1
No. 520 exposure increased to 3.0 in day 4 at 1
*When No. 526 infected, Exposure is 4.0 in day 4 at move 1
*When No. 535 infected, Exposure is 4.0 in day 4 at move 1
*When No. 537 infected, Exposure is 3.0 in day 4 at move 1
No. 540 exposure increased to 1.0 in day 4 at 1
No. 560 exposure increased to 4.0 in day 4 at 1
No. 563 exposure increased to 2.0 in day 4 at 1
No. 569 exposure increased to 5.0 in day 4 at 1
No. 575 exposure increased to 3.0 in day 4 at 1
No. 581 exposure increased to 3.0 in day 4 at 1
No. 584 exposure increased to 4.0 in day 4 at 1
No. 590 exposure increased to 3.0 in day 4 at 1
No. 605 exposure increased to 5.0 in day 4 at 1
No. 611 exposure increased to 3.0 in day 4 at 1
No. 614 exposure increased to 2.0 in day 4 at 1
No. 619 exposure increased to 5.0 in day 4 at 1
*When No. 624 infected, Exposure is 3.0 in day 4 at move 1
No. 636 exposure increased to 1.0 in day 4 at 1
No. 641 exposure increased to 5.0 in day 4 at 1
No. 665 exposure increased to 1.0 in day 4 at 1
No. 668 exposure increased to 1.0 in day 4 at 1
*When No. 672 infected, Exposure is 3.0 in day 4 at move 1
No. 677 exposure increased to 4.0 in day 4 at 1
*When No. 686 infected, Exposure is 3.0 in day 4 at move 1
No. 694 exposure increased to 3.0 in day 4 at 1
No. 696 exposure increased to 3.0 in day 4 at 1
No. 706 exposure increased to 3.0 in day 4 at 1
No. 711 exposure increased to 3.0 in day 4 at 1
No. 735 exposure increased to 2.0 in day 4 at 1
No. 740 exposure increased to 3.0 in day 4 at 1
No. 746 exposure increased to 5.0 in day 4 at 1
No. 750 exposure increased to 2.0 in day 4 at 1
No. 784 exposure increased to 3.0 in day 4 at 1
No. 785 exposure increased to 5.0 in day 4 at 1
No. 789 exposure increased to 6.0 in day 4 at 1
No. 830 exposure increased to 3.0 in day 4 at 1
No. 832 exposure increased to 2.0 in day 4 at 1
No. 833 exposure increased to 3.0 in day 4 at 1
No. 834 exposure increased to 5.0 in day 4 at 1
No. 839 exposure increased to 3.0 in day 4 at 1
No. 842 exposure increased to 3.0 in day 4 at 1
No. 851 exposure increased to 5.0 in day 4 at 1
No. 852 exposure increased to 5.0 in day 4 at 1
*When No. 856 infected, Exposure is 4.0 in day 4 at move 1
No. 858 exposure increased to 5.0 in day 4 at 1
No. 889 exposure increased to 5.0 in day 4 at 1
No. 895 exposure increased to 3.0 in day 4 at 1
No. 899 exposure increased to 3.0 in day 4 at 1
No. 904 exposure increased to 3.0 in day 4 at 1
*When No. 908 infected, Exposure is 3.0 in day 4 at move 1
No. 917 exposure increased to 4.0 in day 4 at 1
No. 929 exposure increased to 1.0 in day 4 at 1
No. 962 exposure increased to 3.0 in day 4 at 1
*When No. 963 infected, Exposure is 6.0 in day 4 at move 1
No. 964 exposure increased to 6.0 in day 4 at 1
No. 965 exposure increased to 3.0 in day 4 at 1
No. 969 exposure increased to 2.0 in day 4 at 1
No. 975 exposure increased to 3.0 in day 4 at 1
No. 990 exposure increased to 1.0 in day 4 at 1
   31/10000 [..............................] - ETA: 29:47:14 - reward: 762.2961*When No. 76 infected, Exposure is 3.0 in day 4 at move 0
*When No. 135 infected, Exposure is 3.0 in day 4 at move 0
*When No. 238 infected, Exposure is 2.0 in day 4 at move 0
*When No. 267 infected, Exposure is 4.0 in day 4 at move 0
*When No. 362 infected, Exposure is 4.0 in day 4 at move 0
*When No. 389 infected, Exposure is 5.0 in day 4 at move 0
*When No. 514 infected, Exposure is 3.0 in day 4 at move 0
*When No. 560 infected, Exposure is 4.0 in day 4 at move 0
*When No. 575 infected, Exposure is 3.0 in day 4 at move 0
*When No. 584 infected, Exposure is 4.0 in day 4 at move 0
*When No. 605 infected, Exposure is 5.0 in day 4 at move 0
*When No. 677 infected, Exposure is 4.0 in day 4 at move 0
*When No. 746 infected, Exposure is 5.0 in day 4 at move 0
*When No. 785 infected, Exposure is 5.0 in day 4 at move 0
*When No. 789 infected, Exposure is 6.0 in day 4 at move 0
*When No. 834 infected, Exposure is 5.0 in day 4 at move 0
*When No. 858 infected, Exposure is 5.0 in day 4 at move 0
*When No. 889 infected, Exposure is 5.0 in day 4 at move 0
*When No. 895 infected, Exposure is 3.0 in day 4 at move 0
*When No. 962 infected, Exposure is 3.0 in day 4 at move 0
*When No. 81 infected, Exposure is 3.0 in day 4 at move 1
*When No. 89 infected, Exposure is 4.0 in day 4 at move 1
*When No. 109 infected, Exposure is 5.0 in day 4 at move 1
*When No. 341 infected, Exposure is 4.0 in day 4 at move 1
*When No. 397 infected, Exposure is 2.0 in day 4 at move 1
*When No. 474 infected, Exposure is 3.0 in day 4 at move 1
*When No. 520 infected, Exposure is 3.0 in day 4 at move 1
*When No. 619 infected, Exposure is 5.0 in day 4 at move 1
*When No. 694 infected, Exposure is 3.0 in day 4 at move 1
*When No. 696 infected, Exposure is 3.0 in day 4 at move 1
*When No. 706 infected, Exposure is 3.0 in day 4 at move 1
*When No. 740 infected, Exposure is 3.0 in day 4 at move 1
*When No. 839 infected, Exposure is 3.0 in day 4 at move 1
*When No. 904 infected, Exposure is 3.0 in day 4 at move 1
*When No. 969 infected, Exposure is 2.0 in day 4 at move 1
*When No. 95 infected, Exposure is 3.0 in day 4 at move 2
*When No. 143 infected, Exposure is 3.0 in day 4 at move 2
*When No. 191 infected, Exposure is 2.0 in day 4 at move 2
*When No. 241 infected, Exposure is 5.0 in day 4 at move 2
*When No. 274 infected, Exposure is 3.0 in day 4 at move 2
*When No. 291 infected, Exposure is 3.0 in day 4 at move 2
*When No. 340 infected, Exposure is 3.0 in day 4 at move 2
*When No. 563 infected, Exposure is 2.0 in day 4 at move 2
*When No. 569 infected, Exposure is 5.0 in day 4 at move 2
*When No. 611 infected, Exposure is 3.0 in day 4 at move 2
*When No. 641 infected, Exposure is 5.0 in day 4 at move 2
*When No. 830 infected, Exposure is 3.0 in day 4 at move 2
*When No. 964 infected, Exposure is 6.0 in day 4 at move 2
*When No. 965 infected, Exposure is 3.0 in day 4 at move 2
*When No. 200 infected, Exposure is 4.0 in day 4 at move 3
*When No. 201 infected, Exposure is 2.0 in day 4 at move 3
*When No. 301 infected, Exposure is 3.0 in day 4 at move 3
*When No. 331 infected, Exposure is 2.0 in day 4 at move 3
*When No. 343 infected, Exposure is 3.0 in day 4 at move 3
*When No. 387 infected, Exposure is 3.0 in day 4 at move 3
*When No. 448 infected, Exposure is 3.0 in day 4 at move 3
*When No. 461 infected, Exposure is 2.0 in day 4 at move 3
*When No. 851 infected, Exposure is 5.0 in day 4 at move 3
*When No. 852 infected, Exposure is 5.0 in day 4 at move 3
*When No. 975 infected, Exposure is 3.0 in day 4 at move 3
*When No. 83 infected, Exposure is 3.0 in day 4 at move 4
*When No. 173 infected, Exposure is 3.0 in day 4 at move 4
*When No. 379 infected, Exposure is 3.0 in day 4 at move 4
*When No. 784 infected, Exposure is 3.0 in day 4 at move 4
*When No. 833 infected, Exposure is 3.0 in day 4 at move 4
No. 0 exposure increased to 2.0 in day 4 at 5
No. 3 exposure increased to 1.0 in day 4 at 5
No. 29 exposure increased to 1.0 in day 4 at 5
No. 48 exposure increased to 1.0 in day 4 at 5
No. 52 exposure increased to 1.0 in day 4 at 5
No. 53 exposure increased to 1.0 in day 4 at 5
No. 68 exposure increased to 1.0 in day 4 at 5
No. 87 exposure increased to 1.0 in day 4 at 5
No. 91 exposure increased to 2.0 in day 4 at 5
No. 94 exposure increased to 4.0 in day 4 at 5
No. 96 exposure increased to 1.0 in day 4 at 5
No. 103 exposure increased to 1.0 in day 4 at 5
No. 106 exposure increased to 4.0 in day 4 at 5
No. 112 exposure increased to 3.0 in day 4 at 5
No. 125 exposure increased to 1.0 in day 4 at 5
No. 128 exposure increased to 1.0 in day 4 at 5
No. 138 exposure increased to 1.0 in day 4 at 5
No. 161 exposure increased to 1.0 in day 4 at 5
No. 166 exposure increased to 2.0 in day 4 at 5
No. 167 exposure increased to 3.0 in day 4 at 5
No. 183 exposure increased to 4.0 in day 4 at 5
No. 185 exposure increased to 1.0 in day 4 at 5
No. 187 exposure increased to 1.0 in day 4 at 5
No. 193 exposure increased to 2.0 in day 4 at 5
No. 202 exposure increased to 1.0 in day 4 at 5
No. 204 exposure increased to 4.0 in day 4 at 5
No. 226 exposure increased to 1.0 in day 4 at 5
No. 234 exposure increased to 2.0 in day 4 at 5
No. 239 exposure increased to 2.0 in day 4 at 5
No. 246 exposure increased to 1.0 in day 4 at 5
No. 260 exposure increased to 3.0 in day 4 at 5
No. 264 exposure increased to 1.0 in day 4 at 5
No. 277 exposure increased to 2.0 in day 4 at 5
No. 278 exposure increased to 1.0 in day 4 at 5
No. 287 exposure increased to 1.0 in day 4 at 5
No. 317 exposure increased to 2.0 in day 4 at 5
No. 338 exposure increased to 2.0 in day 4 at 5
No. 345 exposure increased to 1.0 in day 4 at 5
No. 347 exposure increased to 1.0 in day 4 at 5
No. 350 exposure increased to 2.0 in day 4 at 5
No. 353 exposure increased to 1.0 in day 4 at 5
No. 355 exposure increased to 3.0 in day 4 at 5
No. 386 exposure increased to 1.0 in day 4 at 5
No. 390 exposure increased to 1.0 in day 4 at 5
No. 406 exposure increased to 1.0 in day 4 at 5
No. 407 exposure increased to 1.0 in day 4 at 5
No. 410 exposure increased to 1.0 in day 4 at 5
No. 421 exposure increased to 1.0 in day 4 at 5
No. 431 exposure increased to 1.0 in day 4 at 5
No. 434 exposure increased to 3.0 in day 4 at 5
No. 435 exposure increased to 4.0 in day 4 at 5
No. 443 exposure increased to 1.0 in day 4 at 5
No. 446 exposure increased to 4.0 in day 4 at 5
No. 458 exposure increased to 2.0 in day 4 at 5
No. 469 exposure increased to 3.0 in day 4 at 5
No. 480 exposure increased to 1.0 in day 4 at 5
No. 483 exposure increased to 3.0 in day 4 at 5
No. 502 exposure increased to 2.0 in day 4 at 5
No. 505 exposure increased to 2.0 in day 4 at 5
No. 532 exposure increased to 1.0 in day 4 at 5
No. 540 exposure increased to 2.0 in day 4 at 5
No. 542 exposure increased to 1.0 in day 4 at 5
No. 544 exposure increased to 1.0 in day 4 at 5
No. 581 exposure increased to 4.0 in day 4 at 5
*When No. 590 infected, Exposure is 3.0 in day 4 at move 5
No. 595 exposure increased to 1.0 in day 4 at 5
No. 612 exposure increased to 1.0 in day 4 at 5
*When No. 614 infected, Exposure is 2.0 in day 4 at move 5
No. 615 exposure increased to 2.0 in day 4 at 5
No. 617 exposure increased to 1.0 in day 4 at 5
No. 636 exposure increased to 2.0 in day 4 at 5
No. 639 exposure increased to 1.0 in day 4 at 5
No. 656 exposure increased to 1.0 in day 4 at 5
No. 665 exposure increased to 2.0 in day 4 at 5
No. 668 exposure increased to 2.0 in day 4 at 5
No. 681 exposure increased to 1.0 in day 4 at 5
No. 697 exposure increased to 1.0 in day 4 at 5
No. 700 exposure increased to 1.0 in day 4 at 5
No. 705 exposure increased to 1.0 in day 4 at 5
No. 708 exposure increased to 1.0 in day 4 at 5
*When No. 711 infected, Exposure is 3.0 in day 4 at move 5
No. 715 exposure increased to 1.0 in day 4 at 5
No. 721 exposure increased to 1.0 in day 4 at 5
No. 735 exposure increased to 3.0 in day 4 at 5
No. 737 exposure increased to 2.0 in day 4 at 5
No. 750 exposure increased to 3.0 in day 4 at 5
No. 760 exposure increased to 1.0 in day 4 at 5
No. 795 exposure increased to 1.0 in day 4 at 5
No. 798 exposure increased to 1.0 in day 4 at 5
No. 809 exposure increased to 2.0 in day 4 at 5
No. 823 exposure increased to 1.0 in day 4 at 5
No. 832 exposure increased to 3.0 in day 4 at 5
No. 842 exposure increased to 4.0 in day 4 at 5
No. 843 exposure increased to 1.0 in day 4 at 5
No. 874 exposure increased to 1.0 in day 4 at 5
No. 899 exposure increased to 4.0 in day 4 at 5
No. 910 exposure increased to 1.0 in day 4 at 5
No. 911 exposure increased to 1.0 in day 4 at 5
No. 917 exposure increased to 5.0 in day 4 at 5
No. 922 exposure increased to 1.0 in day 4 at 5
No. 929 exposure increased to 2.0 in day 4 at 5
No. 932 exposure increased to 1.0 in day 4 at 5
No. 982 exposure increased to 1.0 in day 4 at 5
No. 990 exposure increased to 2.0 in day 4 at 5
   32/10000 [..............................] - ETA: 29:39:57 - reward: 747.5006*When No. 166 infected, Exposure is 2.0 in day 4 at move 0
*When No. 204 infected, Exposure is 4.0 in day 4 at move 0
*When No. 260 infected, Exposure is 3.0 in day 4 at move 0
*When No. 355 infected, Exposure is 3.0 in day 4 at move 0
*When No. 615 infected, Exposure is 2.0 in day 4 at move 0
*When No. 809 infected, Exposure is 2.0 in day 4 at move 0
*When No. 842 infected, Exposure is 4.0 in day 4 at move 0
*When No. 899 infected, Exposure is 4.0 in day 4 at move 0
*When No. 0 infected, Exposure is 2.0 in day 4 at move 1
No. 3 exposure increased to 2.0 in day 4 at 1
No. 29 exposure increased to 2.0 in day 4 at 1
No. 48 exposure increased to 2.0 in day 4 at 1
No. 52 exposure increased to 2.0 in day 4 at 1
No. 53 exposure increased to 2.0 in day 4 at 1
No. 68 exposure increased to 2.0 in day 4 at 1
No. 87 exposure increased to 2.0 in day 4 at 1
No. 91 exposure increased to 3.0 in day 4 at 1
No. 94 exposure increased to 5.0 in day 4 at 1
No. 96 exposure increased to 2.0 in day 4 at 1
No. 101 exposure increased to 1.0 in day 4 at 1
No. 103 exposure increased to 2.0 in day 4 at 1
No. 106 exposure increased to 5.0 in day 4 at 1
No. 112 exposure increased to 4.0 in day 4 at 1
No. 121 exposure increased to 1.0 in day 4 at 1
No. 125 exposure increased to 2.0 in day 4 at 1
No. 128 exposure increased to 2.0 in day 4 at 1
No. 138 exposure increased to 2.0 in day 4 at 1
No. 161 exposure increased to 2.0 in day 4 at 1
No. 167 exposure increased to 4.0 in day 4 at 1
No. 183 exposure increased to 5.0 in day 4 at 1
No. 185 exposure increased to 2.0 in day 4 at 1
No. 187 exposure increased to 2.0 in day 4 at 1
No. 193 exposure increased to 3.0 in day 4 at 1
No. 202 exposure increased to 2.0 in day 4 at 1
No. 226 exposure increased to 2.0 in day 4 at 1
No. 234 exposure increased to 3.0 in day 4 at 1
No. 239 exposure increased to 3.0 in day 4 at 1
No. 246 exposure increased to 2.0 in day 4 at 1
No. 264 exposure increased to 2.0 in day 4 at 1
No. 277 exposure increased to 3.0 in day 4 at 1
No. 278 exposure increased to 2.0 in day 4 at 1
No. 287 exposure increased to 2.0 in day 4 at 1
No. 312 exposure increased to 2.0 in day 4 at 1
*When No. 317 infected, Exposure is 2.0 in day 4 at move 1
No. 338 exposure increased to 3.0 in day 4 at 1
No. 345 exposure increased to 2.0 in day 4 at 1
No. 347 exposure increased to 2.0 in day 4 at 1
No. 350 exposure increased to 3.0 in day 4 at 1
No. 352 exposure increased to 1.0 in day 4 at 1
No. 353 exposure increased to 2.0 in day 4 at 1
No. 374 exposure increased to 1.0 in day 4 at 1
No. 386 exposure increased to 2.0 in day 4 at 1
No. 388 exposure increased to 2.0 in day 4 at 1
No. 390 exposure increased to 2.0 in day 4 at 1
No. 406 exposure increased to 2.0 in day 4 at 1
No. 407 exposure increased to 2.0 in day 4 at 1
No. 410 exposure increased to 2.0 in day 4 at 1
No. 421 exposure increased to 2.0 in day 4 at 1
No. 431 exposure increased to 2.0 in day 4 at 1
No. 434 exposure increased to 4.0 in day 4 at 1
No. 435 exposure increased to 5.0 in day 4 at 1
No. 443 exposure increased to 2.0 in day 4 at 1
No. 446 exposure increased to 5.0 in day 4 at 1
No. 458 exposure increased to 3.0 in day 4 at 1
No. 469 exposure increased to 4.0 in day 4 at 1
No. 480 exposure increased to 2.0 in day 4 at 1
No. 483 exposure increased to 4.0 in day 4 at 1
No. 502 exposure increased to 3.0 in day 4 at 1
No. 505 exposure increased to 3.0 in day 4 at 1
No. 506 exposure increased to 1.0 in day 4 at 1
No. 532 exposure increased to 2.0 in day 4 at 1
No. 540 exposure increased to 3.0 in day 4 at 1
No. 542 exposure increased to 2.0 in day 4 at 1
No. 544 exposure increased to 2.0 in day 4 at 1
No. 581 exposure increased to 5.0 in day 4 at 1
No. 595 exposure increased to 2.0 in day 4 at 1
No. 612 exposure increased to 2.0 in day 4 at 1
No. 617 exposure increased to 2.0 in day 4 at 1
*When No. 636 infected, Exposure is 2.0 in day 4 at move 1
No. 639 exposure increased to 2.0 in day 4 at 1
No. 656 exposure increased to 2.0 in day 4 at 1
No. 665 exposure increased to 3.0 in day 4 at 1
No. 668 exposure increased to 3.0 in day 4 at 1
No. 681 exposure increased to 2.0 in day 4 at 1
No. 697 exposure increased to 2.0 in day 4 at 1
No. 699 exposure increased to 1.0 in day 4 at 1
No. 700 exposure increased to 2.0 in day 4 at 1
No. 705 exposure increased to 2.0 in day 4 at 1
No. 708 exposure increased to 2.0 in day 4 at 1
No. 715 exposure increased to 2.0 in day 4 at 1
No. 721 exposure increased to 2.0 in day 4 at 1
No. 735 exposure increased to 4.0 in day 4 at 1
No. 737 exposure increased to 3.0 in day 4 at 1
No. 750 exposure increased to 4.0 in day 4 at 1
No. 759 exposure increased to 2.0 in day 4 at 1
No. 760 exposure increased to 2.0 in day 4 at 1
No. 795 exposure increased to 2.0 in day 4 at 1
No. 798 exposure increased to 2.0 in day 4 at 1
No. 823 exposure increased to 2.0 in day 4 at 1
*When No. 832 infected, Exposure is 3.0 in day 4 at move 1
No. 843 exposure increased to 2.0 in day 4 at 1
No. 868 exposure increased to 2.0 in day 4 at 1
No. 874 exposure increased to 2.0 in day 4 at 1
No. 910 exposure increased to 2.0 in day 4 at 1
No. 911 exposure increased to 2.0 in day 4 at 1
No. 917 exposure increased to 6.0 in day 4 at 1
No. 920 exposure increased to 2.0 in day 4 at 1
No. 922 exposure increased to 2.0 in day 4 at 1
*When No. 929 infected, Exposure is 2.0 in day 4 at move 1
No. 932 exposure increased to 2.0 in day 4 at 1
No. 978 exposure increased to 2.0 in day 4 at 1
No. 982 exposure increased to 2.0 in day 4 at 1
No. 990 exposure increased to 3.0 in day 4 at 1
No. 992 exposure increased to 1.0 in day 4 at 1
   33/10000 [..............................] - ETA: 29:00:08 - reward: 732.8255*When No. 3 infected, Exposure is 2.0 in day 4 at move 0
*When No. 68 infected, Exposure is 2.0 in day 4 at move 0
*When No. 167 infected, Exposure is 4.0 in day 4 at move 0
*When No. 239 infected, Exposure is 3.0 in day 4 at move 0
*When No. 353 infected, Exposure is 2.0 in day 4 at move 0
*When No. 390 infected, Exposure is 2.0 in day 4 at move 0
*When No. 431 infected, Exposure is 2.0 in day 4 at move 0
*When No. 505 infected, Exposure is 3.0 in day 4 at move 0
*When No. 540 infected, Exposure is 3.0 in day 4 at move 0
*When No. 639 infected, Exposure is 2.0 in day 4 at move 0
*When No. 668 infected, Exposure is 3.0 in day 4 at move 0
*When No. 705 infected, Exposure is 2.0 in day 4 at move 0
*When No. 708 infected, Exposure is 2.0 in day 4 at move 0
*When No. 750 infected, Exposure is 4.0 in day 4 at move 0
*When No. 843 infected, Exposure is 2.0 in day 4 at move 0
*When No. 911 infected, Exposure is 2.0 in day 4 at move 0
*When No. 990 infected, Exposure is 3.0 in day 4 at move 0
No. 23 exposure increased to 1.0 in day 4 at 1
No. 29 exposure increased to 3.0 in day 4 at 1
No. 48 exposure increased to 3.0 in day 4 at 1
No. 52 exposure increased to 3.0 in day 4 at 1
*When No. 53 infected, Exposure is 2.0 in day 4 at move 1
No. 87 exposure increased to 3.0 in day 4 at 1
No. 91 exposure increased to 4.0 in day 4 at 1
No. 94 exposure increased to 6.0 in day 4 at 1
*When No. 96 infected, Exposure is 2.0 in day 4 at move 1
No. 101 exposure increased to 2.0 in day 4 at 1
No. 103 exposure increased to 3.0 in day 4 at 1
No. 106 exposure increased to 6.0 in day 4 at 1
No. 112 exposure increased to 5.0 in day 4 at 1
No. 121 exposure increased to 2.0 in day 4 at 1
No. 125 exposure increased to 3.0 in day 4 at 1
No. 128 exposure increased to 3.0 in day 4 at 1
No. 138 exposure increased to 3.0 in day 4 at 1
No. 161 exposure increased to 3.0 in day 4 at 1
*When No. 183 infected, Exposure is 5.0 in day 4 at move 1
No. 185 exposure increased to 3.0 in day 4 at 1
No. 187 exposure increased to 3.0 in day 4 at 1
No. 193 exposure increased to 4.0 in day 4 at 1
No. 202 exposure increased to 3.0 in day 4 at 1
No. 226 exposure increased to 3.0 in day 4 at 1
*When No. 234 infected, Exposure is 3.0 in day 4 at move 1
No. 246 exposure increased to 3.0 in day 4 at 1
No. 253 exposure increased to 1.0 in day 4 at 1
No. 264 exposure increased to 3.0 in day 4 at 1
No. 277 exposure increased to 4.0 in day 4 at 1
No. 278 exposure increased to 3.0 in day 4 at 1
No. 280 exposure increased to 1.0 in day 4 at 1
No. 287 exposure increased to 3.0 in day 4 at 1
No. 312 exposure increased to 3.0 in day 4 at 1
No. 334 exposure increased to 1.0 in day 4 at 1
No. 338 exposure increased to 4.0 in day 4 at 1
No. 345 exposure increased to 3.0 in day 4 at 1
No. 347 exposure increased to 3.0 in day 4 at 1
No. 350 exposure increased to 4.0 in day 4 at 1
No. 352 exposure increased to 2.0 in day 4 at 1
No. 374 exposure increased to 2.0 in day 4 at 1
No. 386 exposure increased to 3.0 in day 4 at 1
No. 388 exposure increased to 3.0 in day 4 at 1
*When No. 406 infected, Exposure is 2.0 in day 4 at move 1
No. 407 exposure increased to 3.0 in day 4 at 1
No. 410 exposure increased to 3.0 in day 4 at 1
*When No. 421 infected, Exposure is 2.0 in day 4 at move 1
*When No. 434 infected, Exposure is 4.0 in day 4 at move 1
No. 435 exposure increased to 6.0 in day 4 at 1
No. 443 exposure increased to 3.0 in day 4 at 1
No. 446 exposure increased to 6.0 in day 4 at 1
No. 457 exposure increased to 1.0 in day 4 at 1
No. 458 exposure increased to 4.0 in day 4 at 1
*When No. 469 infected, Exposure is 4.0 in day 4 at move 1
No. 480 exposure increased to 3.0 in day 4 at 1
No. 483 exposure increased to 5.0 in day 4 at 1
No. 502 exposure increased to 4.0 in day 4 at 1
No. 506 exposure increased to 2.0 in day 4 at 1
No. 532 exposure increased to 3.0 in day 4 at 1
No. 542 exposure increased to 3.0 in day 4 at 1
No. 544 exposure increased to 3.0 in day 4 at 1
No. 564 exposure increased to 2.0 in day 4 at 1
*When No. 581 infected, Exposure is 5.0 in day 4 at move 1
No. 595 exposure increased to 3.0 in day 4 at 1
No. 612 exposure increased to 3.0 in day 4 at 1
No. 617 exposure increased to 3.0 in day 4 at 1
No. 656 exposure increased to 3.0 in day 4 at 1
No. 665 exposure increased to 4.0 in day 4 at 1
No. 681 exposure increased to 3.0 in day 4 at 1
No. 697 exposure increased to 3.0 in day 4 at 1
No. 699 exposure increased to 2.0 in day 4 at 1
No. 700 exposure increased to 3.0 in day 4 at 1
No. 715 exposure increased to 3.0 in day 4 at 1
No. 721 exposure increased to 3.0 in day 4 at 1
*When No. 735 infected, Exposure is 4.0 in day 4 at move 1
No. 737 exposure increased to 4.0 in day 4 at 1
No. 759 exposure increased to 3.0 in day 4 at 1
No. 760 exposure increased to 3.0 in day 4 at 1
No. 767 exposure increased to 1.0 in day 4 at 1
No. 795 exposure increased to 3.0 in day 4 at 1
No. 798 exposure increased to 3.0 in day 4 at 1
No. 814 exposure increased to 2.0 in day 4 at 1
No. 817 exposure increased to 1.0 in day 4 at 1
No. 823 exposure increased to 3.0 in day 4 at 1
No. 841 exposure increased to 1.0 in day 4 at 1
No. 868 exposure increased to 3.0 in day 4 at 1
No. 874 exposure increased to 3.0 in day 4 at 1
No. 910 exposure increased to 3.0 in day 4 at 1
No. 917 exposure increased to 7.0 in day 4 at 1
No. 920 exposure increased to 3.0 in day 4 at 1
No. 922 exposure increased to 3.0 in day 4 at 1
No. 931 exposure increased to 2.0 in day 4 at 1
No. 932 exposure increased to 3.0 in day 4 at 1
No. 978 exposure increased to 3.0 in day 4 at 1
*When No. 982 infected, Exposure is 2.0 in day 4 at move 1
No. 992 exposure increased to 2.0 in day 4 at 1
   34/10000 [..............................] - ETA: 28:21:46 - reward: 718.4976*When No. 48 infected, Exposure is 3.0 in day 4 at move 0
*When No. 91 infected, Exposure is 4.0 in day 4 at move 0
*When No. 94 infected, Exposure is 6.0 in day 4 at move 0
*When No. 106 infected, Exposure is 6.0 in day 4 at move 0
*When No. 138 infected, Exposure is 3.0 in day 4 at move 0
*When No. 185 infected, Exposure is 3.0 in day 4 at move 0
*When No. 187 infected, Exposure is 3.0 in day 4 at move 0
*When No. 277 infected, Exposure is 4.0 in day 4 at move 0
*When No. 278 infected, Exposure is 3.0 in day 4 at move 0
*When No. 350 infected, Exposure is 4.0 in day 4 at move 0
*When No. 446 infected, Exposure is 6.0 in day 4 at move 0
*When No. 483 infected, Exposure is 5.0 in day 4 at move 0
*When No. 502 infected, Exposure is 4.0 in day 4 at move 0
*When No. 542 infected, Exposure is 3.0 in day 4 at move 0
*When No. 544 infected, Exposure is 3.0 in day 4 at move 0
*When No. 617 infected, Exposure is 3.0 in day 4 at move 0
*When No. 759 infected, Exposure is 3.0 in day 4 at move 0
*When No. 760 infected, Exposure is 3.0 in day 4 at move 0
*When No. 920 infected, Exposure is 3.0 in day 4 at move 0
No. 23 exposure increased to 2.0 in day 4 at 1
No. 29 exposure increased to 4.0 in day 4 at 1
No. 52 exposure increased to 4.0 in day 4 at 1
No. 71 exposure increased to 1.0 in day 4 at 1
No. 87 exposure increased to 4.0 in day 4 at 1
No. 101 exposure increased to 3.0 in day 4 at 1
No. 103 exposure increased to 4.0 in day 4 at 1
*When No. 112 infected, Exposure is 5.0 in day 4 at move 1
No. 121 exposure increased to 3.0 in day 4 at 1
*When No. 125 infected, Exposure is 3.0 in day 4 at move 1
No. 128 exposure increased to 4.0 in day 4 at 1
No. 161 exposure increased to 4.0 in day 4 at 1
No. 174 exposure increased to 1.0 in day 4 at 1
No. 193 exposure increased to 5.0 in day 4 at 1
No. 202 exposure increased to 4.0 in day 4 at 1
No. 226 exposure increased to 4.0 in day 4 at 1
No. 240 exposure increased to 1.0 in day 4 at 1
No. 242 exposure increased to 1.0 in day 4 at 1
No. 246 exposure increased to 4.0 in day 4 at 1
No. 253 exposure increased to 2.0 in day 4 at 1
No. 264 exposure increased to 4.0 in day 4 at 1
No. 270 exposure increased to 2.0 in day 4 at 1
No. 280 exposure increased to 2.0 in day 4 at 1
No. 287 exposure increased to 4.0 in day 4 at 1
No. 312 exposure increased to 4.0 in day 4 at 1
No. 324 exposure increased to 1.0 in day 4 at 1
No. 334 exposure increased to 2.0 in day 4 at 1
No. 336 exposure increased to 2.0 in day 4 at 1
*When No. 338 infected, Exposure is 4.0 in day 4 at move 1
*When No. 345 infected, Exposure is 3.0 in day 4 at move 1
No. 347 exposure increased to 4.0 in day 4 at 1
No. 352 exposure increased to 3.0 in day 4 at 1
*When No. 374 infected, Exposure is 2.0 in day 4 at move 1
*When No. 386 infected, Exposure is 3.0 in day 4 at move 1
*When No. 388 infected, Exposure is 3.0 in day 4 at move 1
No. 399 exposure increased to 2.0 in day 4 at 1
No. 402 exposure increased to 1.0 in day 4 at 1
No. 407 exposure increased to 4.0 in day 4 at 1
No. 410 exposure increased to 4.0 in day 4 at 1
No. 418 exposure increased to 1.0 in day 4 at 1
No. 435 exposure increased to 7.0 in day 4 at 1
*When No. 443 infected, Exposure is 3.0 in day 4 at move 1
No. 457 exposure increased to 2.0 in day 4 at 1
No. 458 exposure increased to 5.0 in day 4 at 1
No. 462 exposure increased to 2.0 in day 4 at 1
No. 480 exposure increased to 4.0 in day 4 at 1
No. 506 exposure increased to 3.0 in day 4 at 1
No. 531 exposure increased to 1.0 in day 4 at 1
No. 532 exposure increased to 4.0 in day 4 at 1
No. 564 exposure increased to 3.0 in day 4 at 1
No. 595 exposure increased to 4.0 in day 4 at 1
No. 612 exposure increased to 4.0 in day 4 at 1
No. 656 exposure increased to 4.0 in day 4 at 1
No. 665 exposure increased to 5.0 in day 4 at 1
No. 681 exposure increased to 4.0 in day 4 at 1
No. 697 exposure increased to 4.0 in day 4 at 1
No. 699 exposure increased to 3.0 in day 4 at 1
No. 700 exposure increased to 4.0 in day 4 at 1
*When No. 715 infected, Exposure is 3.0 in day 4 at move 1
*When No. 721 infected, Exposure is 3.0 in day 4 at move 1
No. 737 exposure increased to 5.0 in day 4 at 1
No. 749 exposure increased to 2.0 in day 4 at 1
No. 767 exposure increased to 2.0 in day 4 at 1
*When No. 795 infected, Exposure is 3.0 in day 4 at move 1
No. 798 exposure increased to 4.0 in day 4 at 1
No. 814 exposure increased to 3.0 in day 4 at 1
No. 817 exposure increased to 2.0 in day 4 at 1
No. 818 exposure increased to 2.0 in day 4 at 1
*When No. 823 infected, Exposure is 3.0 in day 4 at move 1
No. 841 exposure increased to 2.0 in day 4 at 1
No. 857 exposure increased to 1.0 in day 4 at 1
No. 868 exposure increased to 4.0 in day 4 at 1
*When No. 874 infected, Exposure is 3.0 in day 4 at move 1
No. 910 exposure increased to 4.0 in day 4 at 1
No. 917 exposure increased to 8.0 in day 4 at 1
No. 922 exposure increased to 4.0 in day 4 at 1
No. 931 exposure increased to 3.0 in day 4 at 1
No. 932 exposure increased to 4.0 in day 4 at 1
No. 953 exposure increased to 2.0 in day 4 at 1
No. 978 exposure increased to 4.0 in day 4 at 1
No. 979 exposure increased to 2.0 in day 4 at 1
No. 992 exposure increased to 3.0 in day 4 at 1
   35/10000 [..............................] - ETA: 27:43:38 - reward: 705.6549*When No. 52 infected, Exposure is 4.0 in day 4 at move 0
*When No. 101 infected, Exposure is 3.0 in day 4 at move 0
*When No. 103 infected, Exposure is 4.0 in day 4 at move 0
*When No. 121 infected, Exposure is 3.0 in day 4 at move 0
*When No. 128 infected, Exposure is 4.0 in day 4 at move 0
*When No. 226 infected, Exposure is 4.0 in day 4 at move 0
*When No. 246 infected, Exposure is 4.0 in day 4 at move 0
*When No. 347 infected, Exposure is 4.0 in day 4 at move 0
*When No. 458 infected, Exposure is 5.0 in day 4 at move 0
*When No. 681 infected, Exposure is 4.0 in day 4 at move 0
*When No. 737 infected, Exposure is 5.0 in day 4 at move 0
*When No. 814 infected, Exposure is 3.0 in day 4 at move 0
*When No. 917 infected, Exposure is 8.0 in day 4 at move 0
*When No. 161 infected, Exposure is 4.0 in day 4 at move 1
*When No. 193 infected, Exposure is 5.0 in day 4 at move 1
*When No. 287 infected, Exposure is 4.0 in day 4 at move 1
*When No. 312 infected, Exposure is 4.0 in day 4 at move 1
*When No. 435 infected, Exposure is 7.0 in day 4 at move 1
*When No. 665 infected, Exposure is 5.0 in day 4 at move 1
*When No. 749 infected, Exposure is 2.0 in day 4 at move 1
*When No. 29 infected, Exposure is 4.0 in day 4 at move 2
*When No. 87 infected, Exposure is 4.0 in day 4 at move 2
*When No. 264 infected, Exposure is 4.0 in day 4 at move 2
*When No. 407 infected, Exposure is 4.0 in day 4 at move 2
*When No. 480 infected, Exposure is 4.0 in day 4 at move 2
*When No. 595 infected, Exposure is 4.0 in day 4 at move 2
*When No. 612 infected, Exposure is 4.0 in day 4 at move 2
*When No. 697 infected, Exposure is 4.0 in day 4 at move 2
*When No. 978 infected, Exposure is 4.0 in day 4 at move 2
*When No. 410 infected, Exposure is 4.0 in day 4 at move 3
*When No. 457 infected, Exposure is 2.0 in day 4 at move 3
*When No. 532 infected, Exposure is 4.0 in day 4 at move 3
*When No. 699 infected, Exposure is 3.0 in day 4 at move 3
*When No. 700 infected, Exposure is 4.0 in day 4 at move 3
*When No. 817 infected, Exposure is 2.0 in day 4 at move 3
*When No. 953 infected, Exposure is 2.0 in day 4 at move 3
*When No. 979 infected, Exposure is 2.0 in day 4 at move 3
*When No. 202 infected, Exposure is 4.0 in day 4 at move 4
*When No. 334 infected, Exposure is 2.0 in day 4 at move 4
*When No. 462 infected, Exposure is 2.0 in day 4 at move 4
*When No. 506 infected, Exposure is 3.0 in day 4 at move 4
*When No. 931 infected, Exposure is 3.0 in day 4 at move 4
No. 23 exposure increased to 3.0 in day 4 at 5
No. 36 exposure increased to 1.0 in day 4 at 5
No. 45 exposure increased to 1.0 in day 4 at 5
No. 71 exposure increased to 2.0 in day 4 at 5
No. 74 exposure increased to 1.0 in day 4 at 5
No. 139 exposure increased to 1.0 in day 4 at 5
No. 155 exposure increased to 1.0 in day 4 at 5
No. 174 exposure increased to 2.0 in day 4 at 5
No. 181 exposure increased to 1.0 in day 4 at 5
No. 188 exposure increased to 1.0 in day 4 at 5
No. 235 exposure increased to 1.0 in day 4 at 5
No. 240 exposure increased to 2.0 in day 4 at 5
No. 242 exposure increased to 2.0 in day 4 at 5
No. 250 exposure increased to 1.0 in day 4 at 5
*When No. 253 infected, Exposure is 2.0 in day 4 at move 5
No. 270 exposure increased to 3.0 in day 4 at 5
No. 273 exposure increased to 1.0 in day 4 at 5
No. 280 exposure increased to 3.0 in day 4 at 5
No. 290 exposure increased to 1.0 in day 4 at 5
No. 320 exposure increased to 1.0 in day 4 at 5
No. 323 exposure increased to 1.0 in day 4 at 5
No. 324 exposure increased to 2.0 in day 4 at 5
No. 332 exposure increased to 1.0 in day 4 at 5
*When No. 336 infected, Exposure is 2.0 in day 4 at move 5
No. 344 exposure increased to 1.0 in day 4 at 5
No. 352 exposure increased to 4.0 in day 4 at 5
No. 399 exposure increased to 3.0 in day 4 at 5
No. 400 exposure increased to 2.0 in day 4 at 5
No. 402 exposure increased to 2.0 in day 4 at 5
No. 412 exposure increased to 2.0 in day 4 at 5
No. 418 exposure increased to 2.0 in day 4 at 5
No. 450 exposure increased to 2.0 in day 4 at 5
No. 452 exposure increased to 2.0 in day 4 at 5
No. 466 exposure increased to 1.0 in day 4 at 5
No. 472 exposure increased to 2.0 in day 4 at 5
No. 477 exposure increased to 1.0 in day 4 at 5
No. 479 exposure increased to 1.0 in day 4 at 5
No. 492 exposure increased to 1.0 in day 4 at 5
No. 531 exposure increased to 2.0 in day 4 at 5
No. 534 exposure increased to 2.0 in day 4 at 5
No. 564 exposure increased to 4.0 in day 4 at 5
No. 603 exposure increased to 2.0 in day 4 at 5
No. 643 exposure increased to 2.0 in day 4 at 5
No. 656 exposure increased to 5.0 in day 4 at 5
No. 676 exposure increased to 2.0 in day 4 at 5
No. 692 exposure increased to 1.0 in day 4 at 5
No. 724 exposure increased to 1.0 in day 4 at 5
No. 728 exposure increased to 1.0 in day 4 at 5
No. 764 exposure increased to 1.0 in day 4 at 5
No. 767 exposure increased to 3.0 in day 4 at 5
No. 790 exposure increased to 1.0 in day 4 at 5
No. 797 exposure increased to 1.0 in day 4 at 5
No. 798 exposure increased to 5.0 in day 4 at 5
No. 818 exposure increased to 3.0 in day 4 at 5
No. 825 exposure increased to 1.0 in day 4 at 5
No. 841 exposure increased to 3.0 in day 4 at 5
No. 857 exposure increased to 2.0 in day 4 at 5
No. 868 exposure increased to 5.0 in day 4 at 5
No. 910 exposure increased to 5.0 in day 4 at 5
No. 921 exposure increased to 1.0 in day 4 at 5
No. 922 exposure increased to 5.0 in day 4 at 5
No. 926 exposure increased to 1.0 in day 4 at 5
No. 932 exposure increased to 5.0 in day 4 at 5
No. 938 exposure increased to 1.0 in day 4 at 5
No. 955 exposure increased to 1.0 in day 4 at 5
No. 956 exposure increased to 2.0 in day 4 at 5
No. 992 exposure increased to 4.0 in day 4 at 5
   36/10000 [..............................] - ETA: 27:26:05 - reward: 691.6256*When No. 23 infected, Exposure is 3.0 in day 4 at move 0
*When No. 399 infected, Exposure is 3.0 in day 4 at move 0
*When No. 676 infected, Exposure is 2.0 in day 4 at move 0
*When No. 798 infected, Exposure is 5.0 in day 4 at move 0
*When No. 868 infected, Exposure is 5.0 in day 4 at move 0
*When No. 910 infected, Exposure is 5.0 in day 4 at move 0
No. 36 exposure increased to 2.0 in day 4 at 1
No. 45 exposure increased to 2.0 in day 4 at 1
No. 71 exposure increased to 3.0 in day 4 at 1
No. 74 exposure increased to 2.0 in day 4 at 1
No. 134 exposure increased to 1.0 in day 4 at 1
No. 139 exposure increased to 2.0 in day 4 at 1
No. 155 exposure increased to 2.0 in day 4 at 1
No. 157 exposure increased to 1.0 in day 4 at 1
No. 174 exposure increased to 3.0 in day 4 at 1
No. 181 exposure increased to 2.0 in day 4 at 1
No. 188 exposure increased to 2.0 in day 4 at 1
No. 222 exposure increased to 1.0 in day 4 at 1
No. 235 exposure increased to 2.0 in day 4 at 1
No. 240 exposure increased to 3.0 in day 4 at 1
No. 242 exposure increased to 3.0 in day 4 at 1
No. 250 exposure increased to 2.0 in day 4 at 1
No. 270 exposure increased to 4.0 in day 4 at 1
No. 273 exposure increased to 2.0 in day 4 at 1
No. 280 exposure increased to 4.0 in day 4 at 1
No. 290 exposure increased to 2.0 in day 4 at 1
No. 320 exposure increased to 2.0 in day 4 at 1
No. 323 exposure increased to 2.0 in day 4 at 1
*When No. 324 infected, Exposure is 2.0 in day 4 at move 1
No. 332 exposure increased to 2.0 in day 4 at 1
No. 344 exposure increased to 2.0 in day 4 at 1
No. 352 exposure increased to 5.0 in day 4 at 1
No. 354 exposure increased to 2.0 in day 4 at 1
No. 367 exposure increased to 2.0 in day 4 at 1
No. 369 exposure increased to 1.0 in day 4 at 1
No. 400 exposure increased to 3.0 in day 4 at 1
No. 402 exposure increased to 3.0 in day 4 at 1
No. 412 exposure increased to 3.0 in day 4 at 1
No. 418 exposure increased to 3.0 in day 4 at 1
No. 450 exposure increased to 3.0 in day 4 at 1
No. 452 exposure increased to 3.0 in day 4 at 1
No. 466 exposure increased to 2.0 in day 4 at 1
No. 472 exposure increased to 3.0 in day 4 at 1
No. 477 exposure increased to 2.0 in day 4 at 1
No. 479 exposure increased to 2.0 in day 4 at 1
No. 492 exposure increased to 2.0 in day 4 at 1
No. 531 exposure increased to 3.0 in day 4 at 1
No. 534 exposure increased to 3.0 in day 4 at 1
*When No. 564 infected, Exposure is 4.0 in day 4 at move 1
No. 603 exposure increased to 3.0 in day 4 at 1
No. 621 exposure increased to 1.0 in day 4 at 1
No. 643 exposure increased to 3.0 in day 4 at 1
*When No. 656 infected, Exposure is 5.0 in day 4 at move 1
No. 692 exposure increased to 2.0 in day 4 at 1
No. 724 exposure increased to 2.0 in day 4 at 1
No. 728 exposure increased to 2.0 in day 4 at 1
No. 729 exposure increased to 1.0 in day 4 at 1
No. 764 exposure increased to 2.0 in day 4 at 1
No. 767 exposure increased to 4.0 in day 4 at 1
No. 790 exposure increased to 2.0 in day 4 at 1
No. 797 exposure increased to 2.0 in day 4 at 1
No. 818 exposure increased to 4.0 in day 4 at 1
No. 825 exposure increased to 2.0 in day 4 at 1
*When No. 841 infected, Exposure is 3.0 in day 4 at move 1
No. 857 exposure increased to 3.0 in day 4 at 1
No. 884 exposure increased to 1.0 in day 4 at 1
No. 921 exposure increased to 2.0 in day 4 at 1
No. 922 exposure increased to 6.0 in day 4 at 1
No. 926 exposure increased to 2.0 in day 4 at 1
*When No. 932 infected, Exposure is 5.0 in day 4 at move 1
No. 938 exposure increased to 2.0 in day 4 at 1
No. 955 exposure increased to 2.0 in day 4 at 1
No. 956 exposure increased to 3.0 in day 4 at 1
*When No. 992 infected, Exposure is 4.0 in day 4 at move 1
   37/10000 [..............................] - ETA: 26:50:39 - reward: 679.1043*When No. 174 infected, Exposure is 3.0 in day 4 at move 0
*When No. 402 infected, Exposure is 3.0 in day 4 at move 0
*When No. 412 infected, Exposure is 3.0 in day 4 at move 0
*When No. 767 infected, Exposure is 4.0 in day 4 at move 0
*When No. 818 infected, Exposure is 4.0 in day 4 at move 0
*When No. 921 infected, Exposure is 2.0 in day 4 at move 0
*When No. 270 infected, Exposure is 4.0 in day 4 at move 1
*When No. 290 infected, Exposure is 2.0 in day 4 at move 1
*When No. 352 infected, Exposure is 5.0 in day 4 at move 1
*When No. 400 infected, Exposure is 3.0 in day 4 at move 1
*When No. 466 infected, Exposure is 2.0 in day 4 at move 1
*When No. 477 infected, Exposure is 2.0 in day 4 at move 1
*When No. 643 infected, Exposure is 3.0 in day 4 at move 1
*When No. 857 infected, Exposure is 3.0 in day 4 at move 1
*When No. 922 infected, Exposure is 6.0 in day 4 at move 1
*When No. 955 infected, Exposure is 2.0 in day 4 at move 1
*When No. 155 infected, Exposure is 2.0 in day 4 at move 2
*When No. 323 infected, Exposure is 2.0 in day 4 at move 2
*When No. 472 infected, Exposure is 3.0 in day 4 at move 2
*When No. 531 infected, Exposure is 3.0 in day 4 at move 2
*When No. 534 infected, Exposure is 3.0 in day 4 at move 2
*When No. 240 infected, Exposure is 3.0 in day 4 at move 3
*When No. 242 infected, Exposure is 3.0 in day 4 at move 3
*When No. 790 infected, Exposure is 2.0 in day 4 at move 3
*When No. 71 infected, Exposure is 3.0 in day 4 at move 4
*When No. 74 infected, Exposure is 2.0 in day 4 at move 4
*When No. 139 infected, Exposure is 2.0 in day 4 at move 4
*When No. 188 infected, Exposure is 2.0 in day 4 at move 4
*When No. 332 infected, Exposure is 2.0 in day 4 at move 4
*When No. 479 infected, Exposure is 2.0 in day 4 at move 4
No. 8 exposure increased to 1.0 in day 4 at 5
No. 36 exposure increased to 3.0 in day 4 at 5
No. 42 exposure increased to 1.0 in day 4 at 5
No. 45 exposure increased to 3.0 in day 4 at 5
No. 134 exposure increased to 2.0 in day 4 at 5
No. 146 exposure increased to 1.0 in day 4 at 5
No. 157 exposure increased to 2.0 in day 4 at 5
No. 181 exposure increased to 3.0 in day 4 at 5
No. 222 exposure increased to 2.0 in day 4 at 5
No. 235 exposure increased to 3.0 in day 4 at 5
No. 237 exposure increased to 1.0 in day 4 at 5
No. 250 exposure increased to 3.0 in day 4 at 5
No. 252 exposure increased to 1.0 in day 4 at 5
No. 273 exposure increased to 3.0 in day 4 at 5
*When No. 280 infected, Exposure is 4.0 in day 4 at move 5
No. 320 exposure increased to 3.0 in day 4 at 5
No. 330 exposure increased to 1.0 in day 4 at 5
*When No. 344 infected, Exposure is 2.0 in day 4 at move 5
No. 354 exposure increased to 3.0 in day 4 at 5
No. 363 exposure increased to 1.0 in day 4 at 5
No. 367 exposure increased to 3.0 in day 4 at 5
No. 369 exposure increased to 2.0 in day 4 at 5
No. 385 exposure increased to 1.0 in day 4 at 5
No. 414 exposure increased to 1.0 in day 4 at 5
No. 418 exposure increased to 4.0 in day 4 at 5
No. 428 exposure increased to 1.0 in day 4 at 5
No. 444 exposure increased to 1.0 in day 4 at 5
No. 450 exposure increased to 4.0 in day 4 at 5
No. 452 exposure increased to 4.0 in day 4 at 5
No. 468 exposure increased to 1.0 in day 4 at 5
No. 492 exposure increased to 3.0 in day 4 at 5
No. 493 exposure increased to 1.0 in day 4 at 5
No. 572 exposure increased to 1.0 in day 4 at 5
No. 603 exposure increased to 4.0 in day 4 at 5
No. 621 exposure increased to 2.0 in day 4 at 5
No. 628 exposure increased to 1.0 in day 4 at 5
No. 635 exposure increased to 1.0 in day 4 at 5
No. 688 exposure increased to 2.0 in day 4 at 5
No. 692 exposure increased to 3.0 in day 4 at 5
No. 704 exposure increased to 1.0 in day 4 at 5
*When No. 724 infected, Exposure is 2.0 in day 4 at move 5
*When No. 728 infected, Exposure is 2.0 in day 4 at move 5
No. 729 exposure increased to 2.0 in day 4 at 5
No. 764 exposure increased to 3.0 in day 4 at 5
No. 773 exposure increased to 1.0 in day 4 at 5
No. 797 exposure increased to 3.0 in day 4 at 5
No. 825 exposure increased to 3.0 in day 4 at 5
No. 845 exposure increased to 2.0 in day 4 at 5
No. 882 exposure increased to 1.0 in day 4 at 5
No. 884 exposure increased to 2.0 in day 4 at 5
No. 926 exposure increased to 3.0 in day 4 at 5
*When No. 938 infected, Exposure is 2.0 in day 4 at move 5
No. 945 exposure increased to 1.0 in day 4 at 5
No. 956 exposure increased to 4.0 in day 4 at 5
   38/10000 [..............................] - ETA: 26:31:21 - reward: 665.8753*When No. 235 infected, Exposure is 3.0 in day 4 at move 0
*When No. 450 infected, Exposure is 4.0 in day 4 at move 0
*When No. 492 infected, Exposure is 3.0 in day 4 at move 0
*When No. 845 infected, Exposure is 2.0 in day 4 at move 0
*When No. 222 infected, Exposure is 2.0 in day 4 at move 1
*When No. 418 infected, Exposure is 4.0 in day 4 at move 1
*When No. 452 infected, Exposure is 4.0 in day 4 at move 1
*When No. 797 infected, Exposure is 3.0 in day 4 at move 1
*When No. 956 infected, Exposure is 4.0 in day 4 at move 1
*When No. 369 infected, Exposure is 2.0 in day 4 at move 2
*When No. 603 infected, Exposure is 4.0 in day 4 at move 2
*When No. 36 infected, Exposure is 3.0 in day 4 at move 3
*When No. 250 infected, Exposure is 3.0 in day 4 at move 3
*When No. 320 infected, Exposure is 3.0 in day 4 at move 3
*When No. 884 infected, Exposure is 2.0 in day 4 at move 3
No. 8 exposure increased to 2.0 in day 4 at 5
No. 9 exposure increased to 1.0 in day 4 at 5
No. 32 exposure increased to 2.0 in day 4 at 5
No. 42 exposure increased to 2.0 in day 4 at 5
No. 45 exposure increased to 4.0 in day 4 at 5
No. 114 exposure increased to 2.0 in day 4 at 5
No. 134 exposure increased to 3.0 in day 4 at 5
No. 146 exposure increased to 2.0 in day 4 at 5
No. 157 exposure increased to 3.0 in day 4 at 5
No. 181 exposure increased to 4.0 in day 4 at 5
No. 192 exposure increased to 1.0 in day 4 at 5
No. 237 exposure increased to 2.0 in day 4 at 5
No. 252 exposure increased to 2.0 in day 4 at 5
No. 273 exposure increased to 4.0 in day 4 at 5
No. 330 exposure increased to 2.0 in day 4 at 5
No. 354 exposure increased to 4.0 in day 4 at 5
No. 357 exposure increased to 1.0 in day 4 at 5
No. 363 exposure increased to 2.0 in day 4 at 5
No. 367 exposure increased to 4.0 in day 4 at 5
No. 378 exposure increased to 1.0 in day 4 at 5
No. 385 exposure increased to 2.0 in day 4 at 5
No. 393 exposure increased to 1.0 in day 4 at 5
No. 414 exposure increased to 2.0 in day 4 at 5
No. 428 exposure increased to 2.0 in day 4 at 5
No. 433 exposure increased to 1.0 in day 4 at 5
No. 444 exposure increased to 2.0 in day 4 at 5
No. 460 exposure increased to 1.0 in day 4 at 5
No. 468 exposure increased to 2.0 in day 4 at 5
No. 493 exposure increased to 2.0 in day 4 at 5
No. 538 exposure increased to 1.0 in day 4 at 5
No. 565 exposure increased to 1.0 in day 4 at 5
No. 572 exposure increased to 2.0 in day 4 at 5
No. 599 exposure increased to 1.0 in day 4 at 5
*When No. 621 infected, Exposure is 2.0 in day 4 at move 5
No. 628 exposure increased to 2.0 in day 4 at 5
No. 631 exposure increased to 1.0 in day 4 at 5
No. 635 exposure increased to 2.0 in day 4 at 5
No. 652 exposure increased to 1.0 in day 4 at 5
No. 688 exposure increased to 3.0 in day 4 at 5
No. 692 exposure increased to 4.0 in day 4 at 5
No. 704 exposure increased to 2.0 in day 4 at 5
No. 729 exposure increased to 3.0 in day 4 at 5
No. 752 exposure increased to 1.0 in day 4 at 5
No. 764 exposure increased to 4.0 in day 4 at 5
No. 773 exposure increased to 2.0 in day 4 at 5
No. 819 exposure increased to 2.0 in day 4 at 5
No. 825 exposure increased to 4.0 in day 4 at 5
No. 849 exposure increased to 1.0 in day 4 at 5
No. 854 exposure increased to 2.0 in day 4 at 5
No. 882 exposure increased to 2.0 in day 4 at 5
No. 887 exposure increased to 1.0 in day 4 at 5
No. 893 exposure increased to 1.0 in day 4 at 5
No. 894 exposure increased to 1.0 in day 4 at 5
No. 896 exposure increased to 2.0 in day 4 at 5
No. 905 exposure increased to 1.0 in day 4 at 5
No. 926 exposure increased to 4.0 in day 4 at 5
No. 945 exposure increased to 2.0 in day 4 at 5
No. 966 exposure increased to 1.0 in day 4 at 5
No. 993 exposure increased to 1.0 in day 4 at 5
   39/10000 [..............................] - ETA: 26:10:49 - reward: 653.8277*When No. 134 infected, Exposure is 3.0 in day 4 at move 0
*When No. 157 infected, Exposure is 3.0 in day 4 at move 0
*When No. 367 infected, Exposure is 4.0 in day 4 at move 0
*When No. 692 infected, Exposure is 4.0 in day 4 at move 0
*When No. 729 infected, Exposure is 3.0 in day 4 at move 0
*When No. 764 infected, Exposure is 4.0 in day 4 at move 0
*When No. 114 infected, Exposure is 2.0 in day 4 at move 1
*When No. 181 infected, Exposure is 4.0 in day 4 at move 1
*When No. 273 infected, Exposure is 4.0 in day 4 at move 1
*When No. 363 infected, Exposure is 2.0 in day 4 at move 1
*When No. 468 infected, Exposure is 2.0 in day 4 at move 1
*When No. 688 infected, Exposure is 3.0 in day 4 at move 1
*When No. 8 infected, Exposure is 2.0 in day 4 at move 2
*When No. 237 infected, Exposure is 2.0 in day 4 at move 2
*When No. 354 infected, Exposure is 4.0 in day 4 at move 2
*When No. 414 infected, Exposure is 2.0 in day 4 at move 2
*When No. 773 infected, Exposure is 2.0 in day 4 at move 2
*When No. 825 infected, Exposure is 4.0 in day 4 at move 2
*When No. 926 infected, Exposure is 4.0 in day 4 at move 2
*When No. 146 infected, Exposure is 2.0 in day 4 at move 4
*When No. 385 infected, Exposure is 2.0 in day 4 at move 4
*When No. 819 infected, Exposure is 2.0 in day 4 at move 4
*When No. 854 infected, Exposure is 2.0 in day 4 at move 4
No. 9 exposure increased to 2.0 in day 4 at 5
No. 26 exposure increased to 2.0 in day 4 at 5
No. 30 exposure increased to 2.0 in day 4 at 5
No. 32 exposure increased to 3.0 in day 4 at 5
No. 42 exposure increased to 3.0 in day 4 at 5
No. 45 exposure increased to 5.0 in day 4 at 5
No. 137 exposure increased to 1.0 in day 4 at 5
No. 165 exposure increased to 2.0 in day 4 at 5
No. 168 exposure increased to 1.0 in day 4 at 5
No. 176 exposure increased to 1.0 in day 4 at 5
No. 192 exposure increased to 2.0 in day 4 at 5
No. 252 exposure increased to 3.0 in day 4 at 5
No. 256 exposure increased to 1.0 in day 4 at 5
*When No. 330 infected, Exposure is 2.0 in day 4 at move 5
No. 357 exposure increased to 2.0 in day 4 at 5
No. 378 exposure increased to 2.0 in day 4 at 5
No. 393 exposure increased to 2.0 in day 4 at 5
No. 428 exposure increased to 3.0 in day 4 at 5
No. 433 exposure increased to 2.0 in day 4 at 5
No. 444 exposure increased to 3.0 in day 4 at 5
No. 460 exposure increased to 2.0 in day 4 at 5
No. 493 exposure increased to 3.0 in day 4 at 5
No. 508 exposure increased to 2.0 in day 4 at 5
No. 530 exposure increased to 1.0 in day 4 at 5
No. 538 exposure increased to 2.0 in day 4 at 5
No. 565 exposure increased to 2.0 in day 4 at 5
No. 572 exposure increased to 3.0 in day 4 at 5
No. 599 exposure increased to 2.0 in day 4 at 5
No. 607 exposure increased to 1.0 in day 4 at 5
No. 628 exposure increased to 3.0 in day 4 at 5
No. 631 exposure increased to 2.0 in day 4 at 5
*When No. 635 infected, Exposure is 2.0 in day 4 at move 5
No. 638 exposure increased to 1.0 in day 4 at 5
No. 652 exposure increased to 2.0 in day 4 at 5
No. 704 exposure increased to 3.0 in day 4 at 5
No. 722 exposure increased to 1.0 in day 4 at 5
No. 752 exposure increased to 2.0 in day 4 at 5
No. 758 exposure increased to 2.0 in day 4 at 5
No. 780 exposure increased to 1.0 in day 4 at 5
No. 806 exposure increased to 2.0 in day 4 at 5
No. 849 exposure increased to 2.0 in day 4 at 5
No. 882 exposure increased to 3.0 in day 4 at 5
No. 887 exposure increased to 2.0 in day 4 at 5
No. 893 exposure increased to 2.0 in day 4 at 5
No. 894 exposure increased to 2.0 in day 4 at 5
No. 896 exposure increased to 3.0 in day 4 at 5
No. 905 exposure increased to 2.0 in day 4 at 5
No. 945 exposure increased to 3.0 in day 4 at 5
No. 966 exposure increased to 2.0 in day 4 at 5
No. 993 exposure increased to 2.0 in day 4 at 5
   40/10000 [..............................] - ETA: 25:49:48 - reward: 642.3320*When No. 32 infected, Exposure is 3.0 in day 4 at move 0
*When No. 42 infected, Exposure is 3.0 in day 4 at move 0
*When No. 45 infected, Exposure is 5.0 in day 4 at move 0
*When No. 252 infected, Exposure is 3.0 in day 4 at move 0
*When No. 428 infected, Exposure is 3.0 in day 4 at move 0
*When No. 538 infected, Exposure is 2.0 in day 4 at move 0
*When No. 945 infected, Exposure is 3.0 in day 4 at move 0
No. 9 exposure increased to 3.0 in day 4 at 1
No. 26 exposure increased to 3.0 in day 4 at 1
No. 30 exposure increased to 3.0 in day 4 at 1
No. 44 exposure increased to 2.0 in day 4 at 1
No. 105 exposure increased to 2.0 in day 4 at 1
No. 137 exposure increased to 2.0 in day 4 at 1
No. 165 exposure increased to 3.0 in day 4 at 1
No. 168 exposure increased to 2.0 in day 4 at 1
No. 176 exposure increased to 2.0 in day 4 at 1
No. 192 exposure increased to 3.0 in day 4 at 1
No. 256 exposure increased to 2.0 in day 4 at 1
No. 357 exposure increased to 3.0 in day 4 at 1
No. 378 exposure increased to 3.0 in day 4 at 1
No. 393 exposure increased to 3.0 in day 4 at 1
No. 433 exposure increased to 3.0 in day 4 at 1
No. 444 exposure increased to 4.0 in day 4 at 1
No. 460 exposure increased to 3.0 in day 4 at 1
No. 493 exposure increased to 4.0 in day 4 at 1
No. 508 exposure increased to 3.0 in day 4 at 1
No. 530 exposure increased to 2.0 in day 4 at 1
No. 561 exposure increased to 2.0 in day 4 at 1
No. 565 exposure increased to 3.0 in day 4 at 1
*When No. 572 infected, Exposure is 3.0 in day 4 at move 1
No. 599 exposure increased to 3.0 in day 4 at 1
No. 607 exposure increased to 2.0 in day 4 at 1
No. 628 exposure increased to 4.0 in day 4 at 1
*When No. 631 infected, Exposure is 2.0 in day 4 at move 1
No. 638 exposure increased to 2.0 in day 4 at 1
No. 652 exposure increased to 3.0 in day 4 at 1
No. 663 exposure increased to 2.0 in day 4 at 1
No. 704 exposure increased to 4.0 in day 4 at 1
No. 722 exposure increased to 2.0 in day 4 at 1
No. 752 exposure increased to 3.0 in day 4 at 1
*When No. 758 infected, Exposure is 2.0 in day 4 at move 1
No. 780 exposure increased to 2.0 in day 4 at 1
No. 806 exposure increased to 3.0 in day 4 at 1
No. 849 exposure increased to 3.0 in day 4 at 1
No. 882 exposure increased to 4.0 in day 4 at 1
No. 887 exposure increased to 3.0 in day 4 at 1
*When No. 893 infected, Exposure is 2.0 in day 4 at move 1
No. 894 exposure increased to 3.0 in day 4 at 1
*When No. 896 infected, Exposure is 3.0 in day 4 at move 1
No. 905 exposure increased to 3.0 in day 4 at 1
No. 966 exposure increased to 3.0 in day 4 at 1
No. 993 exposure increased to 3.0 in day 4 at 1
   41/10000 [..............................] - ETA: 25:17:54 - reward: 631.0446*When No. 26 infected, Exposure is 3.0 in day 4 at move 0
*When No. 44 infected, Exposure is 2.0 in day 4 at move 0
*When No. 165 infected, Exposure is 3.0 in day 4 at move 0
*When No. 393 infected, Exposure is 3.0 in day 4 at move 0
*When No. 433 infected, Exposure is 3.0 in day 4 at move 0
*When No. 561 infected, Exposure is 2.0 in day 4 at move 0
*When No. 565 infected, Exposure is 3.0 in day 4 at move 0
*When No. 599 infected, Exposure is 3.0 in day 4 at move 0
No. 9 exposure increased to 4.0 in day 4 at 1
*When No. 30 infected, Exposure is 3.0 in day 4 at move 1
No. 55 exposure increased to 1.0 in day 4 at 1
No. 105 exposure increased to 3.0 in day 4 at 1
No. 137 exposure increased to 3.0 in day 4 at 1
No. 168 exposure increased to 3.0 in day 4 at 1
*When No. 176 infected, Exposure is 2.0 in day 4 at move 1
No. 192 exposure increased to 4.0 in day 4 at 1
No. 256 exposure increased to 3.0 in day 4 at 1
No. 272 exposure increased to 1.0 in day 4 at 1
No. 293 exposure increased to 2.0 in day 4 at 1
*When No. 357 infected, Exposure is 3.0 in day 4 at move 1
No. 378 exposure increased to 4.0 in day 4 at 1
No. 391 exposure increased to 1.0 in day 4 at 1
No. 444 exposure increased to 5.0 in day 4 at 1
No. 460 exposure increased to 4.0 in day 4 at 1
*When No. 493 infected, Exposure is 4.0 in day 4 at move 1
No. 508 exposure increased to 4.0 in day 4 at 1
No. 530 exposure increased to 3.0 in day 4 at 1
No. 607 exposure increased to 3.0 in day 4 at 1
*When No. 628 infected, Exposure is 4.0 in day 4 at move 1
*When No. 638 infected, Exposure is 2.0 in day 4 at move 1
No. 644 exposure increased to 1.0 in day 4 at 1
No. 652 exposure increased to 4.0 in day 4 at 1
No. 663 exposure increased to 3.0 in day 4 at 1
No. 704 exposure increased to 5.0 in day 4 at 1
No. 722 exposure increased to 3.0 in day 4 at 1
No. 752 exposure increased to 4.0 in day 4 at 1
No. 780 exposure increased to 3.0 in day 4 at 1
No. 806 exposure increased to 4.0 in day 4 at 1
No. 826 exposure increased to 2.0 in day 4 at 1
No. 849 exposure increased to 4.0 in day 4 at 1
No. 882 exposure increased to 5.0 in day 4 at 1
No. 887 exposure increased to 4.0 in day 4 at 1
No. 894 exposure increased to 4.0 in day 4 at 1
No. 905 exposure increased to 4.0 in day 4 at 1
No. 966 exposure increased to 4.0 in day 4 at 1
No. 993 exposure increased to 4.0 in day 4 at 1
   42/10000 [..............................] - ETA: 24:47:25 - reward: 619.9050*When No. 137 infected, Exposure is 3.0 in day 4 at move 0
*When No. 256 infected, Exposure is 3.0 in day 4 at move 0
*When No. 607 infected, Exposure is 3.0 in day 4 at move 0
*When No. 652 infected, Exposure is 4.0 in day 4 at move 0
*When No. 722 infected, Exposure is 3.0 in day 4 at move 0
*When No. 752 infected, Exposure is 4.0 in day 4 at move 0
*When No. 105 infected, Exposure is 3.0 in day 4 at move 1
*When No. 293 infected, Exposure is 2.0 in day 4 at move 1
*When No. 663 infected, Exposure is 3.0 in day 4 at move 1
*When No. 887 infected, Exposure is 4.0 in day 4 at move 1
*When No. 905 infected, Exposure is 4.0 in day 4 at move 1
*When No. 993 infected, Exposure is 4.0 in day 4 at move 1
*When No. 192 infected, Exposure is 4.0 in day 4 at move 2
*When No. 444 infected, Exposure is 5.0 in day 4 at move 2
*When No. 508 infected, Exposure is 4.0 in day 4 at move 2
*When No. 780 infected, Exposure is 3.0 in day 4 at move 2
*When No. 378 infected, Exposure is 4.0 in day 4 at move 3
*When No. 460 infected, Exposure is 4.0 in day 4 at move 3
*When No. 849 infected, Exposure is 4.0 in day 4 at move 3
*When No. 882 infected, Exposure is 5.0 in day 4 at move 3
*When No. 530 infected, Exposure is 3.0 in day 4 at move 4
*When No. 894 infected, Exposure is 4.0 in day 4 at move 4
*When No. 966 infected, Exposure is 4.0 in day 4 at move 4
*When No. 9 infected, Exposure is 4.0 in day 4 at move 5
No. 55 exposure increased to 2.0 in day 4 at 5
No. 66 exposure increased to 2.0 in day 4 at 5
No. 168 exposure increased to 4.0 in day 4 at 5
No. 177 exposure increased to 1.0 in day 4 at 5
No. 272 exposure increased to 2.0 in day 4 at 5
No. 335 exposure increased to 1.0 in day 4 at 5
No. 391 exposure increased to 2.0 in day 4 at 5
No. 519 exposure increased to 1.0 in day 4 at 5
No. 602 exposure increased to 1.0 in day 4 at 5
No. 644 exposure increased to 2.0 in day 4 at 5
*When No. 704 infected, Exposure is 5.0 in day 4 at move 5
No. 717 exposure increased to 1.0 in day 4 at 5
No. 720 exposure increased to 1.0 in day 4 at 5
No. 778 exposure increased to 2.0 in day 4 at 5
No. 806 exposure increased to 5.0 in day 4 at 5
No. 826 exposure increased to 3.0 in day 4 at 5
No. 860 exposure increased to 2.0 in day 4 at 5
No. 891 exposure increased to 1.0 in day 4 at 5
No. 909 exposure increased to 1.0 in day 4 at 5
   43/10000 [..............................] - ETA: 24:27:33 - reward: 610.3453*When No. 272 infected, Exposure is 2.0 in day 4 at move 0
*When No. 806 infected, Exposure is 5.0 in day 4 at move 0
*When No. 391 infected, Exposure is 2.0 in day 4 at move 1
*When No. 644 infected, Exposure is 2.0 in day 4 at move 2
*When No. 860 infected, Exposure is 2.0 in day 4 at move 2
*When No. 55 infected, Exposure is 2.0 in day 4 at move 3
No. 35 exposure increased to 1.0 in day 4 at 5
No. 39 exposure increased to 2.0 in day 4 at 5
No. 66 exposure increased to 3.0 in day 4 at 5
No. 168 exposure increased to 5.0 in day 4 at 5
No. 177 exposure increased to 2.0 in day 4 at 5
No. 228 exposure increased to 1.0 in day 4 at 5
No. 230 exposure increased to 1.0 in day 4 at 5
No. 335 exposure increased to 2.0 in day 4 at 5
No. 470 exposure increased to 1.0 in day 4 at 5
No. 519 exposure increased to 2.0 in day 4 at 5
No. 521 exposure increased to 1.0 in day 4 at 5
No. 522 exposure increased to 1.0 in day 4 at 5
No. 543 exposure increased to 1.0 in day 4 at 5
No. 548 exposure increased to 2.0 in day 4 at 5
No. 602 exposure increased to 2.0 in day 4 at 5
No. 707 exposure increased to 1.0 in day 4 at 5
No. 709 exposure increased to 1.0 in day 4 at 5
No. 717 exposure increased to 2.0 in day 4 at 5
No. 720 exposure increased to 2.0 in day 4 at 5
No. 778 exposure increased to 3.0 in day 4 at 5
No. 826 exposure increased to 4.0 in day 4 at 5
No. 847 exposure increased to 1.0 in day 4 at 5
No. 891 exposure increased to 2.0 in day 4 at 5
No. 909 exposure increased to 2.0 in day 4 at 5
No. 959 exposure increased to 1.0 in day 4 at 5
   44/10000 [..............................] - ETA: 24:06:25 - reward: 602.0866*When No. 548 infected, Exposure is 2.0 in day 4 at move 0
No. 35 exposure increased to 2.0 in day 4 at 1
No. 39 exposure increased to 3.0 in day 4 at 1
*When No. 66 infected, Exposure is 3.0 in day 4 at move 1
No. 168 exposure increased to 6.0 in day 4 at 1
No. 177 exposure increased to 3.0 in day 4 at 1
No. 228 exposure increased to 2.0 in day 4 at 1
No. 230 exposure increased to 2.0 in day 4 at 1
*When No. 335 infected, Exposure is 2.0 in day 4 at move 1
No. 346 exposure increased to 2.0 in day 4 at 1
No. 470 exposure increased to 2.0 in day 4 at 1
No. 519 exposure increased to 3.0 in day 4 at 1
No. 521 exposure increased to 2.0 in day 4 at 1
No. 522 exposure increased to 2.0 in day 4 at 1
No. 533 exposure increased to 2.0 in day 4 at 1
No. 543 exposure increased to 2.0 in day 4 at 1
No. 602 exposure increased to 3.0 in day 4 at 1
No. 654 exposure increased to 1.0 in day 4 at 1
No. 707 exposure increased to 2.0 in day 4 at 1
No. 709 exposure increased to 2.0 in day 4 at 1
No. 717 exposure increased to 3.0 in day 4 at 1
No. 720 exposure increased to 3.0 in day 4 at 1
No. 756 exposure increased to 1.0 in day 4 at 1
No. 778 exposure increased to 4.0 in day 4 at 1
*When No. 826 infected, Exposure is 4.0 in day 4 at move 1
No. 847 exposure increased to 2.0 in day 4 at 1
No. 855 exposure increased to 2.0 in day 4 at 1
No. 891 exposure increased to 3.0 in day 4 at 1
No. 909 exposure increased to 3.0 in day 4 at 1
No. 959 exposure increased to 2.0 in day 4 at 1
   45/10000 [..............................] - ETA: 23:38:38 - reward: 593.9678*When No. 346 infected, Exposure is 2.0 in day 4 at move 0
*When No. 720 infected, Exposure is 3.0 in day 4 at move 0
*When No. 891 infected, Exposure is 3.0 in day 4 at move 0
*When No. 168 infected, Exposure is 6.0 in day 4 at move 1
*When No. 778 infected, Exposure is 4.0 in day 4 at move 1
*When No. 709 infected, Exposure is 2.0 in day 4 at move 2
*When No. 177 infected, Exposure is 3.0 in day 4 at move 3
*When No. 543 infected, Exposure is 2.0 in day 4 at move 3
*When No. 602 infected, Exposure is 3.0 in day 4 at move 3
*When No. 39 infected, Exposure is 3.0 in day 4 at move 4
*When No. 855 infected, Exposure is 2.0 in day 4 at move 4
*When No. 909 infected, Exposure is 3.0 in day 4 at move 4
No. 35 exposure increased to 3.0 in day 4 at 5
No. 141 exposure increased to 1.0 in day 4 at 5
No. 196 exposure increased to 1.0 in day 4 at 5
No. 224 exposure increased to 1.0 in day 4 at 5
No. 228 exposure increased to 3.0 in day 4 at 5
No. 230 exposure increased to 3.0 in day 4 at 5
No. 326 exposure increased to 1.0 in day 4 at 5
No. 451 exposure increased to 1.0 in day 4 at 5
No. 465 exposure increased to 1.0 in day 4 at 5
No. 470 exposure increased to 3.0 in day 4 at 5
No. 519 exposure increased to 4.0 in day 4 at 5
No. 521 exposure increased to 3.0 in day 4 at 5
No. 522 exposure increased to 3.0 in day 4 at 5
No. 533 exposure increased to 3.0 in day 4 at 5
No. 654 exposure increased to 2.0 in day 4 at 5
No. 690 exposure increased to 1.0 in day 4 at 5
No. 707 exposure increased to 3.0 in day 4 at 5
No. 717 exposure increased to 4.0 in day 4 at 5
No. 756 exposure increased to 2.0 in day 4 at 5
No. 838 exposure increased to 1.0 in day 4 at 5
No. 847 exposure increased to 3.0 in day 4 at 5
No. 883 exposure increased to 1.0 in day 4 at 5
No. 959 exposure increased to 3.0 in day 4 at 5
   46/10000 [..............................] - ETA: 23:19:49 - reward: 587.8589*When No. 228 infected, Exposure is 3.0 in day 4 at move 1
*When No. 230 infected, Exposure is 3.0 in day 4 at move 1
*When No. 521 infected, Exposure is 3.0 in day 4 at move 1
*When No. 522 infected, Exposure is 3.0 in day 4 at move 1
*When No. 707 infected, Exposure is 3.0 in day 4 at move 1
*When No. 756 infected, Exposure is 2.0 in day 4 at move 1
*When No. 533 infected, Exposure is 3.0 in day 4 at move 2
*When No. 717 infected, Exposure is 4.0 in day 4 at move 2
*When No. 519 infected, Exposure is 4.0 in day 4 at move 4
*When No. 847 infected, Exposure is 3.0 in day 4 at move 4
*When No. 959 infected, Exposure is 3.0 in day 4 at move 4
No. 35 exposure increased to 4.0 in day 4 at 5
No. 59 exposure increased to 1.0 in day 4 at 5
No. 141 exposure increased to 2.0 in day 4 at 5
No. 196 exposure increased to 2.0 in day 4 at 5
No. 224 exposure increased to 2.0 in day 4 at 5
No. 279 exposure increased to 2.0 in day 4 at 5
No. 326 exposure increased to 2.0 in day 4 at 5
No. 384 exposure increased to 1.0 in day 4 at 5
No. 451 exposure increased to 2.0 in day 4 at 5
No. 465 exposure increased to 2.0 in day 4 at 5
No. 470 exposure increased to 4.0 in day 4 at 5
No. 654 exposure increased to 3.0 in day 4 at 5
No. 690 exposure increased to 2.0 in day 4 at 5
No. 838 exposure increased to 2.0 in day 4 at 5
No. 883 exposure increased to 2.0 in day 4 at 5
   47/10000 [..............................] - ETA: 23:00:28 - reward: 582.9700*When No. 279 infected, Exposure is 2.0 in day 4 at move 0
*When No. 451 infected, Exposure is 2.0 in day 4 at move 0
*When No. 654 infected, Exposure is 3.0 in day 4 at move 0
No. 35 exposure increased to 5.0 in day 4 at 1
No. 59 exposure increased to 2.0 in day 4 at 1
No. 141 exposure increased to 3.0 in day 4 at 1
No. 196 exposure increased to 3.0 in day 4 at 1
No. 224 exposure increased to 3.0 in day 4 at 1
No. 292 exposure increased to 1.0 in day 4 at 1
No. 326 exposure increased to 3.0 in day 4 at 1
No. 384 exposure increased to 2.0 in day 4 at 1
No. 465 exposure increased to 3.0 in day 4 at 1
No. 470 exposure increased to 5.0 in day 4 at 1
No. 690 exposure increased to 3.0 in day 4 at 1
No. 838 exposure increased to 3.0 in day 4 at 1
No. 883 exposure increased to 3.0 in day 4 at 1
   48/10000 [..............................] - ETA: 22:35:32 - reward: 577.4581*When No. 35 infected, Exposure is 5.0 in day 4 at move 0
*When No. 224 infected, Exposure is 3.0 in day 4 at move 0
*When No. 838 infected, Exposure is 3.0 in day 4 at move 0
No. 59 exposure increased to 3.0 in day 4 at 1
No. 141 exposure increased to 4.0 in day 4 at 1
No. 196 exposure increased to 4.0 in day 4 at 1
No. 292 exposure increased to 2.0 in day 4 at 1
No. 326 exposure increased to 4.0 in day 4 at 1
No. 384 exposure increased to 3.0 in day 4 at 1
*When No. 465 infected, Exposure is 3.0 in day 4 at move 1
No. 470 exposure increased to 6.0 in day 4 at 1
No. 588 exposure increased to 2.0 in day 4 at 1
No. 690 exposure increased to 4.0 in day 4 at 1
*When No. 883 infected, Exposure is 3.0 in day 4 at move 1
   49/10000 [..............................] - ETA: 22:11:27 - reward: 573.6080*When No. 470 infected, Exposure is 6.0 in day 4 at move 0
*When No. 326 infected, Exposure is 4.0 in day 4 at move 1
*When No. 59 infected, Exposure is 3.0 in day 4 at move 2
*When No. 141 infected, Exposure is 4.0 in day 4 at move 4
*When No. 690 infected, Exposure is 4.0 in day 4 at move 4
*When No. 196 infected, Exposure is 4.0 in day 4 at move 5
No. 276 exposure increased to 1.0 in day 4 at 5
No. 292 exposure increased to 3.0 in day 4 at 5
No. 384 exposure increased to 4.0 in day 4 at 5
No. 422 exposure increased to 2.0 in day 4 at 5
No. 588 exposure increased to 3.0 in day 4 at 5
   50/10000 [..............................] - ETA: 21:54:20 - reward: 571.7636*When No. 384 infected, Exposure is 4.0 in day 4 at move 0
*When No. 588 infected, Exposure is 3.0 in day 4 at move 0
No. 276 exposure increased to 2.0 in day 4 at 1
No. 292 exposure increased to 4.0 in day 4 at 1
No. 422 exposure increased to 3.0 in day 4 at 1
No. 867 exposure increased to 1.0 in day 4 at 1
   51/10000 [..............................] - ETA: 21:31:38 - reward: 570.1635*When No. 292 infected, Exposure is 4.0 in day 4 at move 0
*When No. 422 infected, Exposure is 3.0 in day 4 at move 3
No. 261 exposure increased to 1.0 in day 4 at 5
No. 276 exposure increased to 3.0 in day 4 at 5
No. 867 exposure increased to 2.0 in day 4 at 5
   52/10000 [..............................] - ETA: 21:14:17 - reward: 568.6540*When No. 276 infected, Exposure is 3.0 in day 4 at move 2
No. 261 exposure increased to 2.0 in day 4 at 5
No. 867 exposure increased to 3.0 in day 4 at 5
   53/10000 [..............................] - ETA: 20:57:21 - reward: 569.8432*When No. 867 infected, Exposure is 3.0 in day 4 at move 2
No. 261 exposure increased to 3.0 in day 4 at 5
   54/10000 [..............................] - ETA: 20:41:24 - reward: 570.1202*When No. 261 infected, Exposure is 3.0 in day 4 at move 2
  101/10000 [..............................] - ETA: 13:10:39 - reward: 702.3737No. 65 exposure increased to 1.0 in day 4 at 5
No. 97 exposure increased to 1.0 in day 4 at 5
No. 158 exposure increased to 1.0 in day 4 at 5
No. 203 exposure increased to 1.0 in day 4 at 5
No. 386 exposure increased to 1.0 in day 4 at 5
No. 430 exposure increased to 1.0 in day 4 at 5
No. 607 exposure increased to 1.0 in day 4 at 5
No. 648 exposure increased to 1.0 in day 4 at 5
No. 675 exposure increased to 1.0 in day 4 at 5
No. 843 exposure increased to 1.0 in day 4 at 5
No. 852 exposure increased to 1.0 in day 4 at 5
  102/10000 [..............................] - ETA: 13:26:30 - reward: 703.9574No. 8 exposure increased to 1.0 in day 4 at 5
No. 25 exposure increased to 1.0 in day 4 at 5
No. 65 exposure increased to 2.0 in day 4 at 5
No. 97 exposure increased to 2.0 in day 4 at 5
No. 136 exposure increased to 1.0 in day 4 at 5
No. 158 exposure increased to 2.0 in day 4 at 5
No. 203 exposure increased to 2.0 in day 4 at 5
No. 386 exposure increased to 2.0 in day 4 at 5
No. 430 exposure increased to 2.0 in day 4 at 5
No. 607 exposure increased to 2.0 in day 4 at 5
No. 648 exposure increased to 2.0 in day 4 at 5
No. 675 exposure increased to 2.0 in day 4 at 5
No. 843 exposure increased to 2.0 in day 4 at 5
No. 852 exposure increased to 2.0 in day 4 at 5
No. 890 exposure increased to 2.0 in day 4 at 5
No. 897 exposure increased to 1.0 in day 4 at 5
  103/10000 [..............................] - ETA: 13:41:45 - reward: 705.6067*When No. 203 infected, Exposure is 2.0 in day 4 at move 0
No. 8 exposure increased to 2.0 in day 4 at 1
No. 25 exposure increased to 2.0 in day 4 at 1
No. 65 exposure increased to 3.0 in day 4 at 1
No. 97 exposure increased to 3.0 in day 4 at 1
No. 136 exposure increased to 2.0 in day 4 at 1
No. 158 exposure increased to 3.0 in day 4 at 1
No. 386 exposure increased to 3.0 in day 4 at 1
No. 430 exposure increased to 3.0 in day 4 at 1
*When No. 607 infected, Exposure is 2.0 in day 4 at move 1
No. 648 exposure increased to 3.0 in day 4 at 1
*When No. 675 infected, Exposure is 2.0 in day 4 at move 1
No. 755 exposure increased to 1.0 in day 4 at 1
*When No. 843 infected, Exposure is 2.0 in day 4 at move 1
*When No. 852 infected, Exposure is 2.0 in day 4 at move 1
No. 890 exposure increased to 3.0 in day 4 at 1
No. 897 exposure increased to 2.0 in day 4 at 1
  104/10000 [..............................] - ETA: 13:41:17 - reward: 707.5620*When No. 8 infected, Exposure is 2.0 in day 4 at move 0
*When No. 97 infected, Exposure is 3.0 in day 4 at move 0
*When No. 430 infected, Exposure is 3.0 in day 4 at move 0
*When No. 648 infected, Exposure is 3.0 in day 4 at move 0
*When No. 386 infected, Exposure is 3.0 in day 4 at move 2
*When No. 136 infected, Exposure is 2.0 in day 4 at move 3
*When No. 25 infected, Exposure is 2.0 in day 4 at move 4
*When No. 158 infected, Exposure is 3.0 in day 4 at move 4
No. 65 exposure increased to 4.0 in day 4 at 5
No. 351 exposure increased to 1.0 in day 4 at 5
No. 755 exposure increased to 2.0 in day 4 at 5
*When No. 890 infected, Exposure is 3.0 in day 4 at move 5
No. 897 exposure increased to 3.0 in day 4 at 5
No. 967 exposure increased to 1.0 in day 4 at 5
No. 977 exposure increased to 1.0 in day 4 at 5
  105/10000 [..............................] - ETA: 13:57:32 - reward: 709.1300*When No. 65 infected, Exposure is 4.0 in day 4 at move 0
No. 46 exposure increased to 1.0 in day 4 at 1
No. 99 exposure increased to 1.0 in day 4 at 1
No. 351 exposure increased to 2.0 in day 4 at 1
No. 361 exposure increased to 1.0 in day 4 at 1
No. 601 exposure increased to 1.0 in day 4 at 1
No. 755 exposure increased to 3.0 in day 4 at 1
No. 886 exposure increased to 1.0 in day 4 at 1
No. 897 exposure increased to 4.0 in day 4 at 1
No. 967 exposure increased to 2.0 in day 4 at 1
No. 977 exposure increased to 2.0 in day 4 at 1
  106/10000 [..............................] - ETA: 13:57:40 - reward: 711.4912*When No. 897 infected, Exposure is 4.0 in day 4 at move 0
No. 46 exposure increased to 2.0 in day 4 at 1
No. 99 exposure increased to 2.0 in day 4 at 1
No. 152 exposure increased to 1.0 in day 4 at 1
No. 165 exposure increased to 2.0 in day 4 at 1
No. 172 exposure increased to 1.0 in day 4 at 1
No. 233 exposure increased to 1.0 in day 4 at 1
No. 351 exposure increased to 3.0 in day 4 at 1
No. 361 exposure increased to 2.0 in day 4 at 1
No. 415 exposure increased to 1.0 in day 4 at 1
No. 564 exposure increased to 1.0 in day 4 at 1
No. 601 exposure increased to 2.0 in day 4 at 1
*When No. 755 infected, Exposure is 3.0 in day 4 at move 1
No. 808 exposure increased to 1.0 in day 4 at 1
No. 813 exposure increased to 2.0 in day 4 at 1
No. 886 exposure increased to 2.0 in day 4 at 1
No. 967 exposure increased to 3.0 in day 4 at 1
No. 970 exposure increased to 2.0 in day 4 at 1
No. 977 exposure increased to 3.0 in day 4 at 1
  107/10000 [..............................] - ETA: 13:57:44 - reward: 713.1508*When No. 361 infected, Exposure is 2.0 in day 4 at move 1
*When No. 46 infected, Exposure is 2.0 in day 4 at move 2
*When No. 977 infected, Exposure is 3.0 in day 4 at move 2
*When No. 99 infected, Exposure is 2.0 in day 4 at move 4
*When No. 886 infected, Exposure is 2.0 in day 4 at move 4
No. 73 exposure increased to 2.0 in day 4 at 5
No. 82 exposure increased to 1.0 in day 4 at 5
No. 133 exposure increased to 1.0 in day 4 at 5
No. 151 exposure increased to 1.0 in day 4 at 5
No. 152 exposure increased to 2.0 in day 4 at 5
No. 165 exposure increased to 3.0 in day 4 at 5
No. 172 exposure increased to 2.0 in day 4 at 5
No. 208 exposure increased to 1.0 in day 4 at 5
No. 233 exposure increased to 2.0 in day 4 at 5
No. 351 exposure increased to 4.0 in day 4 at 5
No. 407 exposure increased to 1.0 in day 4 at 5
No. 415 exposure increased to 2.0 in day 4 at 5
No. 564 exposure increased to 2.0 in day 4 at 5
No. 582 exposure increased to 1.0 in day 4 at 5
No. 601 exposure increased to 3.0 in day 4 at 5
No. 708 exposure increased to 2.0 in day 4 at 5
No. 764 exposure increased to 1.0 in day 4 at 5
No. 781 exposure increased to 1.0 in day 4 at 5
No. 808 exposure increased to 2.0 in day 4 at 5
No. 810 exposure increased to 1.0 in day 4 at 5
No. 813 exposure increased to 3.0 in day 4 at 5
No. 949 exposure increased to 1.0 in day 4 at 5
No. 967 exposure increased to 4.0 in day 4 at 5
No. 970 exposure increased to 3.0 in day 4 at 5
No. 974 exposure increased to 1.0 in day 4 at 5
  108/10000 [..............................] - ETA: 14:12:54 - reward: 713.7698*When No. 73 infected, Exposure is 2.0 in day 4 at move 0
*When No. 351 infected, Exposure is 4.0 in day 4 at move 0
*When No. 152 infected, Exposure is 2.0 in day 4 at move 2
*When No. 601 infected, Exposure is 3.0 in day 4 at move 2
*When No. 708 infected, Exposure is 2.0 in day 4 at move 2
*When No. 813 infected, Exposure is 3.0 in day 4 at move 2
*When No. 808 infected, Exposure is 2.0 in day 4 at move 4
No. 82 exposure increased to 2.0 in day 4 at 5
No. 133 exposure increased to 2.0 in day 4 at 5
No. 151 exposure increased to 2.0 in day 4 at 5
No. 165 exposure increased to 4.0 in day 4 at 5
No. 172 exposure increased to 3.0 in day 4 at 5
No. 208 exposure increased to 2.0 in day 4 at 5
No. 233 exposure increased to 3.0 in day 4 at 5
No. 238 exposure increased to 2.0 in day 4 at 5
No. 290 exposure increased to 1.0 in day 4 at 5
No. 325 exposure increased to 1.0 in day 4 at 5
No. 328 exposure increased to 1.0 in day 4 at 5
No. 381 exposure increased to 1.0 in day 4 at 5
No. 383 exposure increased to 1.0 in day 4 at 5
No. 391 exposure increased to 1.0 in day 4 at 5
No. 395 exposure increased to 1.0 in day 4 at 5
No. 407 exposure increased to 2.0 in day 4 at 5
No. 415 exposure increased to 3.0 in day 4 at 5
No. 564 exposure increased to 3.0 in day 4 at 5
No. 582 exposure increased to 2.0 in day 4 at 5
No. 585 exposure increased to 1.0 in day 4 at 5
No. 603 exposure increased to 1.0 in day 4 at 5
No. 764 exposure increased to 2.0 in day 4 at 5
No. 781 exposure increased to 2.0 in day 4 at 5
No. 810 exposure increased to 2.0 in day 4 at 5
No. 853 exposure increased to 1.0 in day 4 at 5
No. 925 exposure increased to 1.0 in day 4 at 5
No. 938 exposure increased to 2.0 in day 4 at 5
No. 949 exposure increased to 2.0 in day 4 at 5
No. 966 exposure increased to 1.0 in day 4 at 5
*When No. 967 infected, Exposure is 4.0 in day 4 at move 5
No. 970 exposure increased to 4.0 in day 4 at 5
No. 974 exposure increased to 2.0 in day 4 at 5
  109/10000 [..............................] - ETA: 14:29:33 - reward: 715.9246*When No. 165 infected, Exposure is 4.0 in day 4 at move 0
*When No. 233 infected, Exposure is 3.0 in day 4 at move 0
*When No. 781 infected, Exposure is 2.0 in day 4 at move 0
No. 82 exposure increased to 3.0 in day 4 at 1
No. 100 exposure increased to 1.0 in day 4 at 1
No. 133 exposure increased to 3.0 in day 4 at 1
No. 151 exposure increased to 3.0 in day 4 at 1
No. 172 exposure increased to 4.0 in day 4 at 1
No. 208 exposure increased to 3.0 in day 4 at 1
No. 238 exposure increased to 3.0 in day 4 at 1
No. 290 exposure increased to 2.0 in day 4 at 1
No. 325 exposure increased to 2.0 in day 4 at 1
No. 328 exposure increased to 2.0 in day 4 at 1
No. 381 exposure increased to 2.0 in day 4 at 1
No. 383 exposure increased to 2.0 in day 4 at 1
No. 391 exposure increased to 2.0 in day 4 at 1
No. 395 exposure increased to 2.0 in day 4 at 1
*When No. 407 infected, Exposure is 2.0 in day 4 at move 1
No. 415 exposure increased to 4.0 in day 4 at 1
No. 564 exposure increased to 4.0 in day 4 at 1
No. 577 exposure increased to 2.0 in day 4 at 1
No. 582 exposure increased to 3.0 in day 4 at 1
No. 585 exposure increased to 2.0 in day 4 at 1
No. 603 exposure increased to 2.0 in day 4 at 1
No. 764 exposure increased to 3.0 in day 4 at 1
No. 810 exposure increased to 3.0 in day 4 at 1
No. 828 exposure increased to 2.0 in day 4 at 1
No. 853 exposure increased to 2.0 in day 4 at 1
No. 925 exposure increased to 2.0 in day 4 at 1
No. 938 exposure increased to 3.0 in day 4 at 1
No. 949 exposure increased to 3.0 in day 4 at 1
No. 966 exposure increased to 2.0 in day 4 at 1
No. 970 exposure increased to 5.0 in day 4 at 1
*When No. 974 infected, Exposure is 2.0 in day 4 at move 1
  110/10000 [..............................] - ETA: 14:29:27 - reward: 716.4198*When No. 82 infected, Exposure is 3.0 in day 4 at move 0
*When No. 172 infected, Exposure is 4.0 in day 4 at move 0
*When No. 208 infected, Exposure is 3.0 in day 4 at move 0
*When No. 764 infected, Exposure is 3.0 in day 4 at move 0
*When No. 810 infected, Exposure is 3.0 in day 4 at move 0
*When No. 949 infected, Exposure is 3.0 in day 4 at move 0
*When No. 238 infected, Exposure is 3.0 in day 4 at move 1
*When No. 328 infected, Exposure is 2.0 in day 4 at move 1
*When No. 415 infected, Exposure is 4.0 in day 4 at move 1
*When No. 577 infected, Exposure is 2.0 in day 4 at move 1
*When No. 133 infected, Exposure is 3.0 in day 4 at move 2
*When No. 582 infected, Exposure is 3.0 in day 4 at move 2
*When No. 970 infected, Exposure is 5.0 in day 4 at move 2
*When No. 381 infected, Exposure is 2.0 in day 4 at move 3
*When No. 564 infected, Exposure is 4.0 in day 4 at move 3
No. 7 exposure increased to 1.0 in day 4 at 5
No. 52 exposure increased to 1.0 in day 4 at 5
No. 64 exposure increased to 1.0 in day 4 at 5
No. 70 exposure increased to 1.0 in day 4 at 5
No. 75 exposure increased to 1.0 in day 4 at 5
No. 100 exposure increased to 2.0 in day 4 at 5
*When No. 151 infected, Exposure is 3.0 in day 4 at move 5
No. 160 exposure increased to 2.0 in day 4 at 5
No. 200 exposure increased to 1.0 in day 4 at 5
*When No. 290 infected, Exposure is 2.0 in day 4 at move 5
No. 325 exposure increased to 3.0 in day 4 at 5
No. 345 exposure increased to 1.0 in day 4 at 5
No. 383 exposure increased to 3.0 in day 4 at 5
No. 391 exposure increased to 3.0 in day 4 at 5
No. 395 exposure increased to 3.0 in day 4 at 5
No. 422 exposure increased to 2.0 in day 4 at 5
No. 485 exposure increased to 1.0 in day 4 at 5
No. 501 exposure increased to 1.0 in day 4 at 5
No. 549 exposure increased to 1.0 in day 4 at 5
*When No. 585 infected, Exposure is 2.0 in day 4 at move 5
No. 603 exposure increased to 3.0 in day 4 at 5
No. 692 exposure increased to 1.0 in day 4 at 5
No. 713 exposure increased to 1.0 in day 4 at 5
No. 731 exposure increased to 1.0 in day 4 at 5
No. 761 exposure increased to 1.0 in day 4 at 5
No. 775 exposure increased to 1.0 in day 4 at 5
No. 779 exposure increased to 2.0 in day 4 at 5
No. 804 exposure increased to 2.0 in day 4 at 5
*When No. 828 infected, Exposure is 2.0 in day 4 at move 5
No. 853 exposure increased to 3.0 in day 4 at 5
No. 859 exposure increased to 1.0 in day 4 at 5
*When No. 925 infected, Exposure is 2.0 in day 4 at move 5
No. 938 exposure increased to 4.0 in day 4 at 5
No. 966 exposure increased to 3.0 in day 4 at 5
  111/10000 [..............................] - ETA: 14:45:40 - reward: 717.1018*When No. 160 infected, Exposure is 2.0 in day 4 at move 0
*When No. 853 infected, Exposure is 3.0 in day 4 at move 0
No. 7 exposure increased to 2.0 in day 4 at 1
No. 52 exposure increased to 2.0 in day 4 at 1
No. 64 exposure increased to 2.0 in day 4 at 1
No. 70 exposure increased to 2.0 in day 4 at 1
No. 75 exposure increased to 2.0 in day 4 at 1
No. 100 exposure increased to 3.0 in day 4 at 1
No. 200 exposure increased to 2.0 in day 4 at 1
No. 251 exposure increased to 1.0 in day 4 at 1
No. 253 exposure increased to 1.0 in day 4 at 1
No. 325 exposure increased to 4.0 in day 4 at 1
No. 345 exposure increased to 2.0 in day 4 at 1
No. 383 exposure increased to 4.0 in day 4 at 1
No. 391 exposure increased to 4.0 in day 4 at 1
No. 395 exposure increased to 4.0 in day 4 at 1
No. 422 exposure increased to 3.0 in day 4 at 1
No. 454 exposure increased to 2.0 in day 4 at 1
No. 467 exposure increased to 1.0 in day 4 at 1
No. 485 exposure increased to 2.0 in day 4 at 1
No. 497 exposure increased to 1.0 in day 4 at 1
No. 501 exposure increased to 2.0 in day 4 at 1
No. 549 exposure increased to 2.0 in day 4 at 1
No. 552 exposure increased to 1.0 in day 4 at 1
No. 603 exposure increased to 4.0 in day 4 at 1
No. 692 exposure increased to 2.0 in day 4 at 1
No. 713 exposure increased to 2.0 in day 4 at 1
No. 731 exposure increased to 2.0 in day 4 at 1
No. 761 exposure increased to 2.0 in day 4 at 1
No. 775 exposure increased to 2.0 in day 4 at 1
No. 779 exposure increased to 3.0 in day 4 at 1
No. 804 exposure increased to 3.0 in day 4 at 1
No. 844 exposure increased to 1.0 in day 4 at 1
No. 859 exposure increased to 2.0 in day 4 at 1
No. 879 exposure increased to 1.0 in day 4 at 1
No. 938 exposure increased to 5.0 in day 4 at 1
No. 966 exposure increased to 4.0 in day 4 at 1
  112/10000 [..............................] - ETA: 14:45:37 - reward: 718.9329*When No. 345 infected, Exposure is 2.0 in day 4 at move 0
*When No. 501 infected, Exposure is 2.0 in day 4 at move 0
*When No. 966 infected, Exposure is 4.0 in day 4 at move 0
*When No. 52 infected, Exposure is 2.0 in day 4 at move 1
*When No. 75 infected, Exposure is 2.0 in day 4 at move 1
*When No. 200 infected, Exposure is 2.0 in day 4 at move 1
*When No. 775 infected, Exposure is 2.0 in day 4 at move 1
*When No. 325 infected, Exposure is 4.0 in day 4 at move 2
*When No. 804 infected, Exposure is 3.0 in day 4 at move 2
*When No. 938 infected, Exposure is 5.0 in day 4 at move 2
*When No. 395 infected, Exposure is 4.0 in day 4 at move 3
*When No. 422 infected, Exposure is 3.0 in day 4 at move 3
*When No. 731 infected, Exposure is 2.0 in day 4 at move 3
*When No. 454 infected, Exposure is 2.0 in day 4 at move 4
*When No. 761 infected, Exposure is 2.0 in day 4 at move 4
No. 6 exposure increased to 1.0 in day 4 at 5
No. 7 exposure increased to 3.0 in day 4 at 5
No. 23 exposure increased to 1.0 in day 4 at 5
No. 43 exposure increased to 1.0 in day 4 at 5
No. 57 exposure increased to 2.0 in day 4 at 5
No. 64 exposure increased to 3.0 in day 4 at 5
*When No. 70 infected, Exposure is 2.0 in day 4 at move 5
No. 88 exposure increased to 1.0 in day 4 at 5
No. 100 exposure increased to 4.0 in day 4 at 5
No. 218 exposure increased to 2.0 in day 4 at 5
No. 224 exposure increased to 1.0 in day 4 at 5
No. 229 exposure increased to 2.0 in day 4 at 5
No. 251 exposure increased to 2.0 in day 4 at 5
No. 253 exposure increased to 2.0 in day 4 at 5
No. 291 exposure increased to 1.0 in day 4 at 5
No. 310 exposure increased to 1.0 in day 4 at 5
No. 359 exposure increased to 1.0 in day 4 at 5
No. 372 exposure increased to 2.0 in day 4 at 5
No. 383 exposure increased to 5.0 in day 4 at 5
*When No. 391 infected, Exposure is 4.0 in day 4 at move 5
No. 412 exposure increased to 1.0 in day 4 at 5
No. 467 exposure increased to 2.0 in day 4 at 5
No. 473 exposure increased to 1.0 in day 4 at 5
No. 476 exposure increased to 1.0 in day 4 at 5
No. 485 exposure increased to 3.0 in day 4 at 5
No. 497 exposure increased to 2.0 in day 4 at 5
No. 534 exposure increased to 1.0 in day 4 at 5
No. 539 exposure increased to 1.0 in day 4 at 5
No. 549 exposure increased to 3.0 in day 4 at 5
No. 552 exposure increased to 2.0 in day 4 at 5
No. 597 exposure increased to 2.0 in day 4 at 5
No. 603 exposure increased to 5.0 in day 4 at 5
No. 605 exposure increased to 1.0 in day 4 at 5
No. 608 exposure increased to 1.0 in day 4 at 5
No. 692 exposure increased to 3.0 in day 4 at 5
*When No. 713 infected, Exposure is 2.0 in day 4 at move 5
No. 753 exposure increased to 1.0 in day 4 at 5
*When No. 779 infected, Exposure is 3.0 in day 4 at move 5
No. 844 exposure increased to 2.0 in day 4 at 5
No. 859 exposure increased to 3.0 in day 4 at 5
No. 867 exposure increased to 1.0 in day 4 at 5
No. 879 exposure increased to 2.0 in day 4 at 5
No. 891 exposure increased to 1.0 in day 4 at 5
No. 943 exposure increased to 2.0 in day 4 at 5
No. 945 exposure increased to 1.0 in day 4 at 5
No. 964 exposure increased to 1.0 in day 4 at 5
No. 999 exposure increased to 1.0 in day 4 at 5
  113/10000 [..............................] - ETA: 15:00:50 - reward: 719.6692*When No. 383 infected, Exposure is 5.0 in day 4 at move 0
*When No. 467 infected, Exposure is 2.0 in day 4 at move 0
*When No. 485 infected, Exposure is 3.0 in day 4 at move 0
*When No. 552 infected, Exposure is 2.0 in day 4 at move 0
*When No. 859 infected, Exposure is 3.0 in day 4 at move 0
*When No. 879 infected, Exposure is 2.0 in day 4 at move 0
No. 6 exposure increased to 2.0 in day 4 at 1
*When No. 7 infected, Exposure is 3.0 in day 4 at move 1
No. 23 exposure increased to 2.0 in day 4 at 1
No. 43 exposure increased to 2.0 in day 4 at 1
No. 57 exposure increased to 3.0 in day 4 at 1
No. 64 exposure increased to 4.0 in day 4 at 1
No. 88 exposure increased to 2.0 in day 4 at 1
*When No. 100 infected, Exposure is 4.0 in day 4 at move 1
No. 218 exposure increased to 3.0 in day 4 at 1
No. 224 exposure increased to 2.0 in day 4 at 1
No. 229 exposure increased to 3.0 in day 4 at 1
No. 251 exposure increased to 3.0 in day 4 at 1
No. 253 exposure increased to 3.0 in day 4 at 1
No. 256 exposure increased to 1.0 in day 4 at 1
No. 291 exposure increased to 2.0 in day 4 at 1
No. 310 exposure increased to 2.0 in day 4 at 1
No. 359 exposure increased to 2.0 in day 4 at 1
No. 372 exposure increased to 3.0 in day 4 at 1
No. 408 exposure increased to 2.0 in day 4 at 1
No. 412 exposure increased to 2.0 in day 4 at 1
No. 473 exposure increased to 2.0 in day 4 at 1
No. 476 exposure increased to 2.0 in day 4 at 1
No. 497 exposure increased to 3.0 in day 4 at 1
No. 534 exposure increased to 2.0 in day 4 at 1
No. 539 exposure increased to 2.0 in day 4 at 1
No. 549 exposure increased to 4.0 in day 4 at 1
No. 557 exposure increased to 1.0 in day 4 at 1
No. 597 exposure increased to 3.0 in day 4 at 1
No. 603 exposure increased to 6.0 in day 4 at 1
No. 605 exposure increased to 2.0 in day 4 at 1
No. 608 exposure increased to 2.0 in day 4 at 1
No. 642 exposure increased to 2.0 in day 4 at 1
No. 678 exposure increased to 2.0 in day 4 at 1
No. 692 exposure increased to 4.0 in day 4 at 1
No. 707 exposure increased to 1.0 in day 4 at 1
No. 753 exposure increased to 2.0 in day 4 at 1
No. 778 exposure increased to 1.0 in day 4 at 1
No. 836 exposure increased to 1.0 in day 4 at 1
No. 844 exposure increased to 3.0 in day 4 at 1
No. 867 exposure increased to 2.0 in day 4 at 1
No. 878 exposure increased to 1.0 in day 4 at 1
No. 891 exposure increased to 2.0 in day 4 at 1
No. 943 exposure increased to 3.0 in day 4 at 1
No. 945 exposure increased to 2.0 in day 4 at 1
No. 964 exposure increased to 2.0 in day 4 at 1
No. 986 exposure increased to 2.0 in day 4 at 1
No. 999 exposure increased to 2.0 in day 4 at 1
  114/10000 [..............................] - ETA: 15:01:21 - reward: 721.0532*When No. 372 infected, Exposure is 3.0 in day 4 at move 0
*When No. 603 infected, Exposure is 6.0 in day 4 at move 0
*When No. 844 infected, Exposure is 3.0 in day 4 at move 0
*When No. 943 infected, Exposure is 3.0 in day 4 at move 0
*When No. 945 infected, Exposure is 2.0 in day 4 at move 0
No. 6 exposure increased to 3.0 in day 4 at 1
No. 14 exposure increased to 2.0 in day 4 at 1
No. 18 exposure increased to 2.0 in day 4 at 1
No. 23 exposure increased to 3.0 in day 4 at 1
No. 43 exposure increased to 3.0 in day 4 at 1
No. 57 exposure increased to 4.0 in day 4 at 1
No. 64 exposure increased to 5.0 in day 4 at 1
No. 88 exposure increased to 3.0 in day 4 at 1
No. 218 exposure increased to 4.0 in day 4 at 1
No. 224 exposure increased to 3.0 in day 4 at 1
No. 229 exposure increased to 4.0 in day 4 at 1
*When No. 251 infected, Exposure is 3.0 in day 4 at move 1
No. 253 exposure increased to 4.0 in day 4 at 1
No. 256 exposure increased to 2.0 in day 4 at 1
No. 260 exposure increased to 2.0 in day 4 at 1
No. 291 exposure increased to 3.0 in day 4 at 1
No. 310 exposure increased to 3.0 in day 4 at 1
No. 359 exposure increased to 3.0 in day 4 at 1
No. 387 exposure increased to 1.0 in day 4 at 1
No. 408 exposure increased to 3.0 in day 4 at 1
*When No. 412 infected, Exposure is 2.0 in day 4 at move 1
No. 473 exposure increased to 3.0 in day 4 at 1
No. 476 exposure increased to 3.0 in day 4 at 1
No. 497 exposure increased to 4.0 in day 4 at 1
No. 534 exposure increased to 3.0 in day 4 at 1
No. 539 exposure increased to 3.0 in day 4 at 1
No. 549 exposure increased to 5.0 in day 4 at 1
No. 557 exposure increased to 2.0 in day 4 at 1
*When No. 597 infected, Exposure is 3.0 in day 4 at move 1
No. 605 exposure increased to 3.0 in day 4 at 1
No. 608 exposure increased to 3.0 in day 4 at 1
*When No. 642 infected, Exposure is 2.0 in day 4 at move 1
No. 678 exposure increased to 3.0 in day 4 at 1
*When No. 692 infected, Exposure is 4.0 in day 4 at move 1
No. 707 exposure increased to 2.0 in day 4 at 1
*When No. 753 infected, Exposure is 2.0 in day 4 at move 1
No. 778 exposure increased to 2.0 in day 4 at 1
No. 836 exposure increased to 2.0 in day 4 at 1
No. 867 exposure increased to 3.0 in day 4 at 1
No. 878 exposure increased to 2.0 in day 4 at 1
No. 891 exposure increased to 3.0 in day 4 at 1
No. 964 exposure increased to 3.0 in day 4 at 1
No. 986 exposure increased to 3.0 in day 4 at 1
No. 995 exposure increased to 1.0 in day 4 at 1
No. 999 exposure increased to 3.0 in day 4 at 1
  115/10000 [..............................] - ETA: 15:01:22 - reward: 722.0857*When No. 64 infected, Exposure is 5.0 in day 4 at move 0
*When No. 229 infected, Exposure is 4.0 in day 4 at move 0
*When No. 253 infected, Exposure is 4.0 in day 4 at move 0
*When No. 497 infected, Exposure is 4.0 in day 4 at move 0
*When No. 534 infected, Exposure is 3.0 in day 4 at move 0
*When No. 57 infected, Exposure is 4.0 in day 4 at move 1
*When No. 549 infected, Exposure is 5.0 in day 4 at move 1
*When No. 605 infected, Exposure is 3.0 in day 4 at move 1
*When No. 878 infected, Exposure is 2.0 in day 4 at move 1
*When No. 986 infected, Exposure is 3.0 in day 4 at move 1
*When No. 88 infected, Exposure is 3.0 in day 4 at move 2
*When No. 218 infected, Exposure is 4.0 in day 4 at move 2
*When No. 291 infected, Exposure is 3.0 in day 4 at move 2
*When No. 778 infected, Exposure is 2.0 in day 4 at move 2
*When No. 18 infected, Exposure is 2.0 in day 4 at move 3
*When No. 260 infected, Exposure is 2.0 in day 4 at move 3
*When No. 310 infected, Exposure is 3.0 in day 4 at move 3
*When No. 473 infected, Exposure is 3.0 in day 4 at move 3
*When No. 539 infected, Exposure is 3.0 in day 4 at move 3
*When No. 891 infected, Exposure is 3.0 in day 4 at move 3
*When No. 408 infected, Exposure is 3.0 in day 4 at move 4
*When No. 476 infected, Exposure is 3.0 in day 4 at move 4
*When No. 836 infected, Exposure is 2.0 in day 4 at move 4
*When No. 6 infected, Exposure is 3.0 in day 4 at move 5
No. 14 exposure increased to 3.0 in day 4 at 5
No. 23 exposure increased to 4.0 in day 4 at 5
No. 43 exposure increased to 4.0 in day 4 at 5
No. 51 exposure increased to 1.0 in day 4 at 5
No. 106 exposure increased to 1.0 in day 4 at 5
No. 110 exposure increased to 1.0 in day 4 at 5
No. 176 exposure increased to 1.0 in day 4 at 5
No. 193 exposure increased to 1.0 in day 4 at 5
No. 224 exposure increased to 4.0 in day 4 at 5
No. 232 exposure increased to 1.0 in day 4 at 5
No. 256 exposure increased to 3.0 in day 4 at 5
No. 267 exposure increased to 1.0 in day 4 at 5
No. 271 exposure increased to 2.0 in day 4 at 5
No. 348 exposure increased to 1.0 in day 4 at 5
No. 358 exposure increased to 2.0 in day 4 at 5
No. 359 exposure increased to 4.0 in day 4 at 5
No. 387 exposure increased to 2.0 in day 4 at 5
No. 396 exposure increased to 2.0 in day 4 at 5
No. 424 exposure increased to 2.0 in day 4 at 5
No. 432 exposure increased to 1.0 in day 4 at 5
No. 461 exposure increased to 2.0 in day 4 at 5
No. 486 exposure increased to 1.0 in day 4 at 5
No. 490 exposure increased to 1.0 in day 4 at 5
No. 491 exposure increased to 1.0 in day 4 at 5
No. 524 exposure increased to 1.0 in day 4 at 5
No. 526 exposure increased to 2.0 in day 4 at 5
No. 532 exposure increased to 1.0 in day 4 at 5
No. 533 exposure increased to 1.0 in day 4 at 5
No. 536 exposure increased to 1.0 in day 4 at 5
No. 540 exposure increased to 1.0 in day 4 at 5
No. 542 exposure increased to 1.0 in day 4 at 5
No. 557 exposure increased to 3.0 in day 4 at 5
No. 566 exposure increased to 1.0 in day 4 at 5
No. 590 exposure increased to 1.0 in day 4 at 5
No. 608 exposure increased to 4.0 in day 4 at 5
No. 645 exposure increased to 1.0 in day 4 at 5
No. 678 exposure increased to 4.0 in day 4 at 5
No. 684 exposure increased to 1.0 in day 4 at 5
No. 703 exposure increased to 2.0 in day 4 at 5
No. 707 exposure increased to 3.0 in day 4 at 5
No. 709 exposure increased to 1.0 in day 4 at 5
No. 766 exposure increased to 1.0 in day 4 at 5
No. 831 exposure increased to 2.0 in day 4 at 5
No. 867 exposure increased to 4.0 in day 4 at 5
No. 913 exposure increased to 1.0 in day 4 at 5
No. 930 exposure increased to 2.0 in day 4 at 5
No. 947 exposure increased to 1.0 in day 4 at 5
No. 964 exposure increased to 4.0 in day 4 at 5
No. 984 exposure increased to 1.0 in day 4 at 5
No. 989 exposure increased to 1.0 in day 4 at 5
No. 995 exposure increased to 2.0 in day 4 at 5
*When No. 999 infected, Exposure is 3.0 in day 4 at move 5
  116/10000 [..............................] - ETA: 15:17:30 - reward: 721.9916*When No. 43 infected, Exposure is 4.0 in day 4 at move 0
*When No. 256 infected, Exposure is 3.0 in day 4 at move 0
*When No. 678 infected, Exposure is 4.0 in day 4 at move 0
*When No. 703 infected, Exposure is 2.0 in day 4 at move 0
*When No. 930 infected, Exposure is 2.0 in day 4 at move 0
*When No. 995 infected, Exposure is 2.0 in day 4 at move 0
*When No. 271 infected, Exposure is 2.0 in day 4 at move 1
*When No. 526 infected, Exposure is 2.0 in day 4 at move 1
*When No. 14 infected, Exposure is 3.0 in day 4 at move 2
*When No. 224 infected, Exposure is 4.0 in day 4 at move 2
*When No. 359 infected, Exposure is 4.0 in day 4 at move 2
*When No. 831 infected, Exposure is 2.0 in day 4 at move 2
*When No. 461 infected, Exposure is 2.0 in day 4 at move 3
*When No. 707 infected, Exposure is 3.0 in day 4 at move 3
*When No. 964 infected, Exposure is 4.0 in day 4 at move 3
*When No. 608 infected, Exposure is 4.0 in day 4 at move 4
*When No. 867 infected, Exposure is 4.0 in day 4 at move 4
No. 23 exposure increased to 5.0 in day 4 at 5
No. 51 exposure increased to 2.0 in day 4 at 5
No. 106 exposure increased to 2.0 in day 4 at 5
No. 110 exposure increased to 2.0 in day 4 at 5
No. 131 exposure increased to 1.0 in day 4 at 5
No. 154 exposure increased to 1.0 in day 4 at 5
No. 176 exposure increased to 2.0 in day 4 at 5
No. 193 exposure increased to 2.0 in day 4 at 5
No. 207 exposure increased to 1.0 in day 4 at 5
No. 211 exposure increased to 1.0 in day 4 at 5
No. 213 exposure increased to 1.0 in day 4 at 5
No. 225 exposure increased to 1.0 in day 4 at 5
No. 232 exposure increased to 2.0 in day 4 at 5
No. 236 exposure increased to 1.0 in day 4 at 5
No. 267 exposure increased to 2.0 in day 4 at 5
No. 268 exposure increased to 1.0 in day 4 at 5
No. 301 exposure increased to 1.0 in day 4 at 5
No. 331 exposure increased to 1.0 in day 4 at 5
No. 338 exposure increased to 1.0 in day 4 at 5
No. 348 exposure increased to 2.0 in day 4 at 5
No. 352 exposure increased to 1.0 in day 4 at 5
No. 358 exposure increased to 3.0 in day 4 at 5
No. 377 exposure increased to 2.0 in day 4 at 5
No. 387 exposure increased to 3.0 in day 4 at 5
*When No. 396 infected, Exposure is 2.0 in day 4 at move 5
No. 424 exposure increased to 3.0 in day 4 at 5
No. 432 exposure increased to 2.0 in day 4 at 5
No. 453 exposure increased to 1.0 in day 4 at 5
No. 455 exposure increased to 1.0 in day 4 at 5
No. 486 exposure increased to 2.0 in day 4 at 5
No. 490 exposure increased to 2.0 in day 4 at 5
No. 491 exposure increased to 2.0 in day 4 at 5
No. 524 exposure increased to 2.0 in day 4 at 5
No. 529 exposure increased to 1.0 in day 4 at 5
No. 532 exposure increased to 2.0 in day 4 at 5
No. 533 exposure increased to 2.0 in day 4 at 5
No. 536 exposure increased to 2.0 in day 4 at 5
No. 540 exposure increased to 2.0 in day 4 at 5
No. 542 exposure increased to 2.0 in day 4 at 5
No. 557 exposure increased to 4.0 in day 4 at 5
No. 566 exposure increased to 2.0 in day 4 at 5
No. 590 exposure increased to 2.0 in day 4 at 5
No. 598 exposure increased to 1.0 in day 4 at 5
No. 610 exposure increased to 1.0 in day 4 at 5
No. 612 exposure increased to 1.0 in day 4 at 5
No. 628 exposure increased to 2.0 in day 4 at 5
No. 645 exposure increased to 2.0 in day 4 at 5
No. 684 exposure increased to 2.0 in day 4 at 5
No. 699 exposure increased to 1.0 in day 4 at 5
No. 709 exposure increased to 2.0 in day 4 at 5
No. 722 exposure increased to 1.0 in day 4 at 5
No. 734 exposure increased to 1.0 in day 4 at 5
No. 744 exposure increased to 1.0 in day 4 at 5
No. 766 exposure increased to 2.0 in day 4 at 5
No. 791 exposure increased to 1.0 in day 4 at 5
No. 855 exposure increased to 1.0 in day 4 at 5
No. 896 exposure increased to 1.0 in day 4 at 5
No. 910 exposure increased to 1.0 in day 4 at 5
No. 913 exposure increased to 2.0 in day 4 at 5
No. 917 exposure increased to 1.0 in day 4 at 5
No. 934 exposure increased to 1.0 in day 4 at 5
No. 944 exposure increased to 1.0 in day 4 at 5
No. 947 exposure increased to 2.0 in day 4 at 5
No. 984 exposure increased to 2.0 in day 4 at 5
No. 989 exposure increased to 2.0 in day 4 at 5
  117/10000 [..............................] - ETA: 15:34:09 - reward: 721.9951*When No. 106 infected, Exposure is 2.0 in day 4 at move 0
*When No. 540 infected, Exposure is 2.0 in day 4 at move 0
*When No. 628 infected, Exposure is 2.0 in day 4 at move 0
*When No. 913 infected, Exposure is 2.0 in day 4 at move 0
*When No. 23 infected, Exposure is 5.0 in day 4 at move 1
*When No. 387 infected, Exposure is 3.0 in day 4 at move 1
*When No. 566 infected, Exposure is 2.0 in day 4 at move 1
*When No. 193 infected, Exposure is 2.0 in day 4 at move 2
*When No. 557 infected, Exposure is 4.0 in day 4 at move 2
*When No. 984 infected, Exposure is 2.0 in day 4 at move 2
*When No. 51 infected, Exposure is 2.0 in day 4 at move 3
*When No. 358 infected, Exposure is 3.0 in day 4 at move 3
*When No. 424 infected, Exposure is 3.0 in day 4 at move 3
*When No. 491 infected, Exposure is 2.0 in day 4 at move 3
*When No. 377 infected, Exposure is 2.0 in day 4 at move 4
No. 9 exposure increased to 1.0 in day 4 at 5
No. 10 exposure increased to 1.0 in day 4 at 5
No. 45 exposure increased to 1.0 in day 4 at 5
No. 84 exposure increased to 1.0 in day 4 at 5
No. 110 exposure increased to 3.0 in day 4 at 5
No. 117 exposure increased to 1.0 in day 4 at 5
No. 127 exposure increased to 1.0 in day 4 at 5
No. 131 exposure increased to 2.0 in day 4 at 5
No. 154 exposure increased to 2.0 in day 4 at 5
No. 157 exposure increased to 1.0 in day 4 at 5
No. 176 exposure increased to 3.0 in day 4 at 5
No. 202 exposure increased to 1.0 in day 4 at 5
No. 207 exposure increased to 2.0 in day 4 at 5
No. 211 exposure increased to 2.0 in day 4 at 5
No. 213 exposure increased to 2.0 in day 4 at 5
No. 225 exposure increased to 2.0 in day 4 at 5
No. 232 exposure increased to 3.0 in day 4 at 5
No. 236 exposure increased to 2.0 in day 4 at 5
No. 258 exposure increased to 1.0 in day 4 at 5
No. 262 exposure increased to 2.0 in day 4 at 5
*When No. 267 infected, Exposure is 2.0 in day 4 at move 5
No. 268 exposure increased to 2.0 in day 4 at 5
No. 280 exposure increased to 1.0 in day 4 at 5
No. 283 exposure increased to 1.0 in day 4 at 5
No. 292 exposure increased to 1.0 in day 4 at 5
No. 301 exposure increased to 2.0 in day 4 at 5
No. 331 exposure increased to 2.0 in day 4 at 5
No. 338 exposure increased to 2.0 in day 4 at 5
No. 343 exposure increased to 1.0 in day 4 at 5
No. 346 exposure increased to 1.0 in day 4 at 5
No. 348 exposure increased to 3.0 in day 4 at 5
No. 352 exposure increased to 2.0 in day 4 at 5
No. 385 exposure increased to 1.0 in day 4 at 5
No. 420 exposure increased to 1.0 in day 4 at 5
No. 432 exposure increased to 3.0 in day 4 at 5
No. 445 exposure increased to 1.0 in day 4 at 5
No. 453 exposure increased to 2.0 in day 4 at 5
No. 455 exposure increased to 2.0 in day 4 at 5
No. 486 exposure increased to 3.0 in day 4 at 5
*When No. 490 infected, Exposure is 2.0 in day 4 at move 5
No. 492 exposure increased to 1.0 in day 4 at 5
No. 513 exposure increased to 1.0 in day 4 at 5
*When No. 524 infected, Exposure is 2.0 in day 4 at move 5
No. 529 exposure increased to 2.0 in day 4 at 5
*When No. 532 infected, Exposure is 2.0 in day 4 at move 5
No. 533 exposure increased to 3.0 in day 4 at 5
No. 536 exposure increased to 3.0 in day 4 at 5
No. 542 exposure increased to 3.0 in day 4 at 5
No. 554 exposure increased to 2.0 in day 4 at 5
No. 558 exposure increased to 1.0 in day 4 at 5
No. 590 exposure increased to 3.0 in day 4 at 5
No. 596 exposure increased to 1.0 in day 4 at 5
No. 598 exposure increased to 2.0 in day 4 at 5
No. 610 exposure increased to 2.0 in day 4 at 5
No. 612 exposure increased to 2.0 in day 4 at 5
No. 614 exposure increased to 1.0 in day 4 at 5
No. 638 exposure increased to 2.0 in day 4 at 5
No. 645 exposure increased to 3.0 in day 4 at 5
No. 684 exposure increased to 3.0 in day 4 at 5
No. 699 exposure increased to 2.0 in day 4 at 5
*When No. 709 infected, Exposure is 2.0 in day 4 at move 5
No. 722 exposure increased to 2.0 in day 4 at 5
No. 734 exposure increased to 2.0 in day 4 at 5
No. 744 exposure increased to 2.0 in day 4 at 5
No. 749 exposure increased to 1.0 in day 4 at 5
No. 762 exposure increased to 1.0 in day 4 at 5
No. 766 exposure increased to 3.0 in day 4 at 5
No. 788 exposure increased to 1.0 in day 4 at 5
No. 791 exposure increased to 2.0 in day 4 at 5
No. 816 exposure increased to 1.0 in day 4 at 5
No. 820 exposure increased to 2.0 in day 4 at 5
No. 855 exposure increased to 2.0 in day 4 at 5
No. 872 exposure increased to 1.0 in day 4 at 5
No. 896 exposure increased to 2.0 in day 4 at 5
No. 910 exposure increased to 2.0 in day 4 at 5
No. 917 exposure increased to 2.0 in day 4 at 5
No. 934 exposure increased to 2.0 in day 4 at 5
No. 936 exposure increased to 1.0 in day 4 at 5
No. 944 exposure increased to 2.0 in day 4 at 5
No. 947 exposure increased to 3.0 in day 4 at 5
No. 989 exposure increased to 3.0 in day 4 at 5
  118/10000 [..............................] - ETA: 15:49:42 - reward: 722.2121*When No. 213 infected, Exposure is 2.0 in day 4 at move 0
*When No. 262 infected, Exposure is 2.0 in day 4 at move 0
*When No. 348 infected, Exposure is 3.0 in day 4 at move 0
*When No. 533 infected, Exposure is 3.0 in day 4 at move 0
*When No. 536 infected, Exposure is 3.0 in day 4 at move 0
*When No. 722 infected, Exposure is 2.0 in day 4 at move 0
*When No. 947 infected, Exposure is 3.0 in day 4 at move 0
No. 9 exposure increased to 2.0 in day 4 at 1
No. 10 exposure increased to 2.0 in day 4 at 1
No. 45 exposure increased to 2.0 in day 4 at 1
No. 84 exposure increased to 2.0 in day 4 at 1
No. 98 exposure increased to 1.0 in day 4 at 1
No. 101 exposure increased to 2.0 in day 4 at 1
No. 110 exposure increased to 4.0 in day 4 at 1
No. 117 exposure increased to 2.0 in day 4 at 1
No. 127 exposure increased to 2.0 in day 4 at 1
No. 131 exposure increased to 3.0 in day 4 at 1
No. 137 exposure increased to 2.0 in day 4 at 1
No. 154 exposure increased to 3.0 in day 4 at 1
No. 157 exposure increased to 2.0 in day 4 at 1
No. 163 exposure increased to 1.0 in day 4 at 1
*When No. 176 infected, Exposure is 3.0 in day 4 at move 1
No. 202 exposure increased to 2.0 in day 4 at 1
No. 207 exposure increased to 3.0 in day 4 at 1
No. 211 exposure increased to 3.0 in day 4 at 1
No. 225 exposure increased to 3.0 in day 4 at 1
No. 232 exposure increased to 4.0 in day 4 at 1
No. 236 exposure increased to 3.0 in day 4 at 1
No. 258 exposure increased to 2.0 in day 4 at 1
No. 268 exposure increased to 3.0 in day 4 at 1
No. 280 exposure increased to 2.0 in day 4 at 1
No. 283 exposure increased to 2.0 in day 4 at 1
No. 292 exposure increased to 2.0 in day 4 at 1
No. 301 exposure increased to 3.0 in day 4 at 1
No. 331 exposure increased to 3.0 in day 4 at 1
No. 338 exposure increased to 3.0 in day 4 at 1
No. 343 exposure increased to 2.0 in day 4 at 1
No. 346 exposure increased to 2.0 in day 4 at 1
No. 352 exposure increased to 3.0 in day 4 at 1
No. 385 exposure increased to 2.0 in day 4 at 1
No. 420 exposure increased to 2.0 in day 4 at 1
No. 432 exposure increased to 4.0 in day 4 at 1
No. 445 exposure increased to 2.0 in day 4 at 1
No. 453 exposure increased to 3.0 in day 4 at 1
No. 455 exposure increased to 3.0 in day 4 at 1
No. 486 exposure increased to 4.0 in day 4 at 1
No. 492 exposure increased to 2.0 in day 4 at 1
No. 513 exposure increased to 2.0 in day 4 at 1
No. 529 exposure increased to 3.0 in day 4 at 1
No. 542 exposure increased to 4.0 in day 4 at 1
No. 554 exposure increased to 3.0 in day 4 at 1
No. 558 exposure increased to 2.0 in day 4 at 1
No. 590 exposure increased to 4.0 in day 4 at 1
No. 596 exposure increased to 2.0 in day 4 at 1
*When No. 598 infected, Exposure is 2.0 in day 4 at move 1
No. 610 exposure increased to 3.0 in day 4 at 1
No. 612 exposure increased to 3.0 in day 4 at 1
No. 614 exposure increased to 2.0 in day 4 at 1
*When No. 638 infected, Exposure is 2.0 in day 4 at move 1
No. 645 exposure increased to 4.0 in day 4 at 1
No. 677 exposure increased to 1.0 in day 4 at 1
*When No. 684 infected, Exposure is 3.0 in day 4 at move 1
No. 699 exposure increased to 3.0 in day 4 at 1
No. 706 exposure increased to 2.0 in day 4 at 1
No. 734 exposure increased to 3.0 in day 4 at 1
No. 744 exposure increased to 3.0 in day 4 at 1
No. 749 exposure increased to 2.0 in day 4 at 1
No. 762 exposure increased to 2.0 in day 4 at 1
No. 766 exposure increased to 4.0 in day 4 at 1
No. 788 exposure increased to 2.0 in day 4 at 1
No. 791 exposure increased to 3.0 in day 4 at 1
No. 816 exposure increased to 2.0 in day 4 at 1
No. 820 exposure increased to 3.0 in day 4 at 1
No. 855 exposure increased to 3.0 in day 4 at 1
No. 872 exposure increased to 2.0 in day 4 at 1
No. 888 exposure increased to 1.0 in day 4 at 1
No. 896 exposure increased to 3.0 in day 4 at 1
*When No. 910 infected, Exposure is 2.0 in day 4 at move 1
No. 917 exposure increased to 3.0 in day 4 at 1
No. 934 exposure increased to 3.0 in day 4 at 1
No. 936 exposure increased to 2.0 in day 4 at 1
No. 944 exposure increased to 3.0 in day 4 at 1
No. 989 exposure increased to 4.0 in day 4 at 1
  119/10000 [..............................] - ETA: 15:49:50 - reward: 722.6140*When No. 45 infected, Exposure is 2.0 in day 4 at move 0
*When No. 211 infected, Exposure is 3.0 in day 4 at move 0
*When No. 236 infected, Exposure is 3.0 in day 4 at move 0
*When No. 292 infected, Exposure is 2.0 in day 4 at move 0
*When No. 432 infected, Exposure is 4.0 in day 4 at move 0
*When No. 455 infected, Exposure is 3.0 in day 4 at move 0
*When No. 486 infected, Exposure is 4.0 in day 4 at move 0
*When No. 645 infected, Exposure is 4.0 in day 4 at move 0
*When No. 699 infected, Exposure is 3.0 in day 4 at move 0
*When No. 766 infected, Exposure is 4.0 in day 4 at move 0
*When No. 816 infected, Exposure is 2.0 in day 4 at move 0
*When No. 896 infected, Exposure is 3.0 in day 4 at move 0
No. 9 exposure increased to 3.0 in day 4 at 1
No. 10 exposure increased to 3.0 in day 4 at 1
No. 55 exposure increased to 2.0 in day 4 at 1
*When No. 84 infected, Exposure is 2.0 in day 4 at move 1
No. 98 exposure increased to 2.0 in day 4 at 1
No. 101 exposure increased to 3.0 in day 4 at 1
No. 110 exposure increased to 5.0 in day 4 at 1
No. 117 exposure increased to 3.0 in day 4 at 1
No. 127 exposure increased to 3.0 in day 4 at 1
No. 131 exposure increased to 4.0 in day 4 at 1
*When No. 137 infected, Exposure is 2.0 in day 4 at move 1
No. 154 exposure increased to 4.0 in day 4 at 1
No. 157 exposure increased to 3.0 in day 4 at 1
No. 163 exposure increased to 2.0 in day 4 at 1
No. 169 exposure increased to 1.0 in day 4 at 1
No. 197 exposure increased to 1.0 in day 4 at 1
No. 202 exposure increased to 3.0 in day 4 at 1
*When No. 207 infected, Exposure is 3.0 in day 4 at move 1
No. 210 exposure increased to 1.0 in day 4 at 1
*When No. 225 infected, Exposure is 3.0 in day 4 at move 1
No. 232 exposure increased to 5.0 in day 4 at 1
No. 258 exposure increased to 3.0 in day 4 at 1
No. 268 exposure increased to 4.0 in day 4 at 1
No. 280 exposure increased to 3.0 in day 4 at 1
No. 283 exposure increased to 3.0 in day 4 at 1
No. 301 exposure increased to 4.0 in day 4 at 1
No. 331 exposure increased to 4.0 in day 4 at 1
No. 338 exposure increased to 4.0 in day 4 at 1
No. 343 exposure increased to 3.0 in day 4 at 1
*When No. 346 infected, Exposure is 2.0 in day 4 at move 1
No. 352 exposure increased to 4.0 in day 4 at 1
No. 378 exposure increased to 2.0 in day 4 at 1
No. 385 exposure increased to 3.0 in day 4 at 1
No. 404 exposure increased to 2.0 in day 4 at 1
No. 420 exposure increased to 3.0 in day 4 at 1
No. 445 exposure increased to 3.0 in day 4 at 1
No. 453 exposure increased to 4.0 in day 4 at 1
No. 492 exposure increased to 3.0 in day 4 at 1
No. 513 exposure increased to 3.0 in day 4 at 1
*When No. 529 infected, Exposure is 3.0 in day 4 at move 1
No. 542 exposure increased to 5.0 in day 4 at 1
No. 554 exposure increased to 4.0 in day 4 at 1
No. 558 exposure increased to 3.0 in day 4 at 1
*When No. 590 infected, Exposure is 4.0 in day 4 at move 1
No. 596 exposure increased to 3.0 in day 4 at 1
No. 610 exposure increased to 4.0 in day 4 at 1
*When No. 612 infected, Exposure is 3.0 in day 4 at move 1
*When No. 614 infected, Exposure is 2.0 in day 4 at move 1
No. 629 exposure increased to 2.0 in day 4 at 1
No. 640 exposure increased to 2.0 in day 4 at 1
No. 651 exposure increased to 2.0 in day 4 at 1
No. 677 exposure increased to 2.0 in day 4 at 1
No. 706 exposure increased to 3.0 in day 4 at 1
No. 715 exposure increased to 1.0 in day 4 at 1
No. 734 exposure increased to 4.0 in day 4 at 1
No. 744 exposure increased to 4.0 in day 4 at 1
No. 749 exposure increased to 3.0 in day 4 at 1
No. 762 exposure increased to 3.0 in day 4 at 1
No. 774 exposure increased to 1.0 in day 4 at 1
No. 788 exposure increased to 3.0 in day 4 at 1
No. 791 exposure increased to 4.0 in day 4 at 1
No. 820 exposure increased to 4.0 in day 4 at 1
No. 855 exposure increased to 4.0 in day 4 at 1
No. 872 exposure increased to 3.0 in day 4 at 1
No. 888 exposure increased to 2.0 in day 4 at 1
*When No. 917 infected, Exposure is 3.0 in day 4 at move 1
No. 934 exposure increased to 4.0 in day 4 at 1
No. 936 exposure increased to 3.0 in day 4 at 1
No. 944 exposure increased to 4.0 in day 4 at 1
*When No. 989 infected, Exposure is 4.0 in day 4 at move 1
  120/10000 [..............................] - ETA: 15:50:03 - reward: 722.2943*When No. 9 infected, Exposure is 3.0 in day 4 at move 0
*When No. 127 infected, Exposure is 3.0 in day 4 at move 0
*When No. 131 infected, Exposure is 4.0 in day 4 at move 0
*When No. 232 infected, Exposure is 5.0 in day 4 at move 0
*When No. 268 infected, Exposure is 4.0 in day 4 at move 0
*When No. 283 infected, Exposure is 3.0 in day 4 at move 0
*When No. 378 infected, Exposure is 2.0 in day 4 at move 0
*When No. 385 infected, Exposure is 3.0 in day 4 at move 0
*When No. 492 infected, Exposure is 3.0 in day 4 at move 0
*When No. 542 infected, Exposure is 5.0 in day 4 at move 0
*When No. 554 infected, Exposure is 4.0 in day 4 at move 0
*When No. 596 infected, Exposure is 3.0 in day 4 at move 0
*When No. 706 infected, Exposure is 3.0 in day 4 at move 0
*When No. 788 infected, Exposure is 3.0 in day 4 at move 0
*When No. 791 infected, Exposure is 4.0 in day 4 at move 0
No. 10 exposure increased to 4.0 in day 4 at 1
No. 13 exposure increased to 1.0 in day 4 at 1
No. 55 exposure increased to 3.0 in day 4 at 1
No. 98 exposure increased to 3.0 in day 4 at 1
No. 101 exposure increased to 4.0 in day 4 at 1
*When No. 110 infected, Exposure is 5.0 in day 4 at move 1
No. 117 exposure increased to 4.0 in day 4 at 1
*When No. 154 infected, Exposure is 4.0 in day 4 at move 1
No. 157 exposure increased to 4.0 in day 4 at 1
No. 163 exposure increased to 3.0 in day 4 at 1
No. 169 exposure increased to 2.0 in day 4 at 1
No. 197 exposure increased to 2.0 in day 4 at 1
No. 202 exposure increased to 4.0 in day 4 at 1
No. 210 exposure increased to 2.0 in day 4 at 1
No. 258 exposure increased to 4.0 in day 4 at 1
No. 272 exposure increased to 2.0 in day 4 at 1
No. 280 exposure increased to 4.0 in day 4 at 1
*When No. 301 infected, Exposure is 4.0 in day 4 at move 1
No. 331 exposure increased to 5.0 in day 4 at 1
*When No. 338 infected, Exposure is 4.0 in day 4 at move 1
No. 343 exposure increased to 4.0 in day 4 at 1
*When No. 352 infected, Exposure is 4.0 in day 4 at move 1
No. 366 exposure increased to 1.0 in day 4 at 1
No. 404 exposure increased to 3.0 in day 4 at 1
No. 420 exposure increased to 4.0 in day 4 at 1
*When No. 445 infected, Exposure is 3.0 in day 4 at move 1
*When No. 453 infected, Exposure is 4.0 in day 4 at move 1
No. 508 exposure increased to 2.0 in day 4 at 1
No. 513 exposure increased to 4.0 in day 4 at 1
No. 558 exposure increased to 4.0 in day 4 at 1
No. 610 exposure increased to 5.0 in day 4 at 1
No. 629 exposure increased to 3.0 in day 4 at 1
No. 640 exposure increased to 3.0 in day 4 at 1
No. 651 exposure increased to 3.0 in day 4 at 1
No. 658 exposure increased to 2.0 in day 4 at 1
No. 668 exposure increased to 1.0 in day 4 at 1
*When No. 677 infected, Exposure is 2.0 in day 4 at move 1
No. 715 exposure increased to 2.0 in day 4 at 1
*When No. 734 infected, Exposure is 4.0 in day 4 at move 1
No. 744 exposure increased to 5.0 in day 4 at 1
No. 749 exposure increased to 4.0 in day 4 at 1
No. 762 exposure increased to 4.0 in day 4 at 1
No. 774 exposure increased to 2.0 in day 4 at 1
No. 820 exposure increased to 5.0 in day 4 at 1
No. 832 exposure increased to 2.0 in day 4 at 1
No. 834 exposure increased to 1.0 in day 4 at 1
No. 855 exposure increased to 5.0 in day 4 at 1
No. 872 exposure increased to 4.0 in day 4 at 1
No. 888 exposure increased to 3.0 in day 4 at 1
No. 895 exposure increased to 1.0 in day 4 at 1
No. 927 exposure increased to 1.0 in day 4 at 1
*When No. 934 infected, Exposure is 4.0 in day 4 at move 1
No. 936 exposure increased to 4.0 in day 4 at 1
*When No. 944 infected, Exposure is 4.0 in day 4 at move 1
No. 988 exposure increased to 1.0 in day 4 at 1
  121/10000 [..............................] - ETA: 15:50:14 - reward: 721.9404*When No. 10 infected, Exposure is 4.0 in day 4 at move 0
*When No. 163 infected, Exposure is 3.0 in day 4 at move 0
*When No. 258 infected, Exposure is 4.0 in day 4 at move 0
*When No. 331 infected, Exposure is 5.0 in day 4 at move 0
*When No. 343 infected, Exposure is 4.0 in day 4 at move 0
*When No. 420 infected, Exposure is 4.0 in day 4 at move 0
*When No. 774 infected, Exposure is 2.0 in day 4 at move 0
*When No. 855 infected, Exposure is 5.0 in day 4 at move 0
*When No. 101 infected, Exposure is 4.0 in day 4 at move 1
*When No. 157 infected, Exposure is 4.0 in day 4 at move 1
*When No. 513 infected, Exposure is 4.0 in day 4 at move 1
*When No. 610 infected, Exposure is 5.0 in day 4 at move 1
*When No. 744 infected, Exposure is 5.0 in day 4 at move 1
*When No. 820 infected, Exposure is 5.0 in day 4 at move 1
*When No. 872 infected, Exposure is 4.0 in day 4 at move 1
*When No. 117 infected, Exposure is 4.0 in day 4 at move 2
*When No. 169 infected, Exposure is 2.0 in day 4 at move 2
*When No. 280 infected, Exposure is 4.0 in day 4 at move 2
*When No. 651 infected, Exposure is 3.0 in day 4 at move 2
*When No. 762 infected, Exposure is 4.0 in day 4 at move 2
*When No. 55 infected, Exposure is 3.0 in day 4 at move 3
*When No. 629 infected, Exposure is 3.0 in day 4 at move 3
*When No. 936 infected, Exposure is 4.0 in day 4 at move 3
*When No. 404 infected, Exposure is 3.0 in day 4 at move 4
*When No. 558 infected, Exposure is 4.0 in day 4 at move 4
No. 11 exposure increased to 1.0 in day 4 at 5
No. 13 exposure increased to 2.0 in day 4 at 5
No. 31 exposure increased to 2.0 in day 4 at 5
No. 77 exposure increased to 2.0 in day 4 at 5
*When No. 98 infected, Exposure is 3.0 in day 4 at move 5
No. 105 exposure increased to 1.0 in day 4 at 5
No. 132 exposure increased to 2.0 in day 4 at 5
No. 179 exposure increased to 1.0 in day 4 at 5
No. 197 exposure increased to 3.0 in day 4 at 5
No. 201 exposure increased to 1.0 in day 4 at 5
No. 202 exposure increased to 5.0 in day 4 at 5
No. 210 exposure increased to 3.0 in day 4 at 5
No. 226 exposure increased to 1.0 in day 4 at 5
No. 231 exposure increased to 1.0 in day 4 at 5
No. 265 exposure increased to 1.0 in day 4 at 5
No. 272 exposure increased to 3.0 in day 4 at 5
No. 299 exposure increased to 1.0 in day 4 at 5
No. 312 exposure increased to 1.0 in day 4 at 5
No. 314 exposure increased to 1.0 in day 4 at 5
No. 316 exposure increased to 1.0 in day 4 at 5
No. 366 exposure increased to 2.0 in day 4 at 5
No. 388 exposure increased to 2.0 in day 4 at 5
No. 406 exposure increased to 1.0 in day 4 at 5
No. 428 exposure increased to 1.0 in day 4 at 5
No. 463 exposure increased to 1.0 in day 4 at 5
No. 464 exposure increased to 2.0 in day 4 at 5
No. 470 exposure increased to 1.0 in day 4 at 5
No. 481 exposure increased to 1.0 in day 4 at 5
No. 508 exposure increased to 3.0 in day 4 at 5
No. 515 exposure increased to 1.0 in day 4 at 5
No. 541 exposure increased to 1.0 in day 4 at 5
No. 551 exposure increased to 1.0 in day 4 at 5
No. 565 exposure increased to 1.0 in day 4 at 5
No. 570 exposure increased to 2.0 in day 4 at 5
No. 573 exposure increased to 2.0 in day 4 at 5
No. 581 exposure increased to 1.0 in day 4 at 5
No. 584 exposure increased to 1.0 in day 4 at 5
No. 604 exposure increased to 1.0 in day 4 at 5
No. 640 exposure increased to 4.0 in day 4 at 5
No. 658 exposure increased to 3.0 in day 4 at 5
No. 668 exposure increased to 2.0 in day 4 at 5
No. 715 exposure increased to 3.0 in day 4 at 5
No. 720 exposure increased to 1.0 in day 4 at 5
No. 721 exposure increased to 1.0 in day 4 at 5
No. 727 exposure increased to 1.0 in day 4 at 5
No. 736 exposure increased to 1.0 in day 4 at 5
*When No. 749 infected, Exposure is 4.0 in day 4 at move 5
No. 763 exposure increased to 1.0 in day 4 at 5
No. 792 exposure increased to 1.0 in day 4 at 5
No. 807 exposure increased to 1.0 in day 4 at 5
No. 819 exposure increased to 1.0 in day 4 at 5
No. 821 exposure increased to 1.0 in day 4 at 5
No. 826 exposure increased to 1.0 in day 4 at 5
No. 832 exposure increased to 3.0 in day 4 at 5
No. 834 exposure increased to 2.0 in day 4 at 5
No. 847 exposure increased to 1.0 in day 4 at 5
No. 873 exposure increased to 1.0 in day 4 at 5
No. 880 exposure increased to 1.0 in day 4 at 5
No. 885 exposure increased to 2.0 in day 4 at 5
*When No. 888 infected, Exposure is 3.0 in day 4 at move 5
No. 895 exposure increased to 2.0 in day 4 at 5
No. 901 exposure increased to 1.0 in day 4 at 5
No. 923 exposure increased to 1.0 in day 4 at 5
No. 927 exposure increased to 2.0 in day 4 at 5
No. 968 exposure increased to 1.0 in day 4 at 5
No. 969 exposure increased to 1.0 in day 4 at 5
No. 988 exposure increased to 2.0 in day 4 at 5
  122/10000 [..............................] - ETA: 16:06:25 - reward: 721.3926*When No. 272 infected, Exposure is 3.0 in day 4 at move 0
*When No. 640 infected, Exposure is 4.0 in day 4 at move 0
*When No. 668 infected, Exposure is 2.0 in day 4 at move 0
*When No. 464 infected, Exposure is 2.0 in day 4 at move 1
*When No. 202 infected, Exposure is 5.0 in day 4 at move 2
*When No. 832 infected, Exposure is 3.0 in day 4 at move 2
*When No. 31 infected, Exposure is 2.0 in day 4 at move 3
*When No. 77 infected, Exposure is 2.0 in day 4 at move 3
*When No. 132 infected, Exposure is 2.0 in day 4 at move 3
*When No. 197 infected, Exposure is 3.0 in day 4 at move 3
*When No. 715 infected, Exposure is 3.0 in day 4 at move 3
*When No. 366 infected, Exposure is 2.0 in day 4 at move 4
*When No. 658 infected, Exposure is 3.0 in day 4 at move 4
*When No. 885 infected, Exposure is 2.0 in day 4 at move 4
No. 11 exposure increased to 2.0 in day 4 at 5
No. 13 exposure increased to 3.0 in day 4 at 5
No. 54 exposure increased to 1.0 in day 4 at 5
No. 62 exposure increased to 1.0 in day 4 at 5
No. 68 exposure increased to 1.0 in day 4 at 5
No. 69 exposure increased to 1.0 in day 4 at 5
No. 92 exposure increased to 2.0 in day 4 at 5
No. 105 exposure increased to 2.0 in day 4 at 5
No. 107 exposure increased to 2.0 in day 4 at 5
No. 120 exposure increased to 1.0 in day 4 at 5
No. 166 exposure increased to 1.0 in day 4 at 5
No. 175 exposure increased to 1.0 in day 4 at 5
No. 179 exposure increased to 2.0 in day 4 at 5
No. 183 exposure increased to 1.0 in day 4 at 5
No. 201 exposure increased to 2.0 in day 4 at 5
No. 210 exposure increased to 4.0 in day 4 at 5
No. 220 exposure increased to 1.0 in day 4 at 5
No. 226 exposure increased to 2.0 in day 4 at 5
No. 228 exposure increased to 2.0 in day 4 at 5
No. 231 exposure increased to 2.0 in day 4 at 5
No. 265 exposure increased to 2.0 in day 4 at 5
No. 299 exposure increased to 2.0 in day 4 at 5
No. 306 exposure increased to 2.0 in day 4 at 5
No. 312 exposure increased to 2.0 in day 4 at 5
No. 314 exposure increased to 2.0 in day 4 at 5
No. 316 exposure increased to 2.0 in day 4 at 5
No. 317 exposure increased to 1.0 in day 4 at 5
No. 355 exposure increased to 1.0 in day 4 at 5
No. 388 exposure increased to 3.0 in day 4 at 5
No. 394 exposure increased to 1.0 in day 4 at 5
No. 406 exposure increased to 2.0 in day 4 at 5
No. 419 exposure increased to 1.0 in day 4 at 5
No. 426 exposure increased to 1.0 in day 4 at 5
No. 428 exposure increased to 2.0 in day 4 at 5
No. 439 exposure increased to 1.0 in day 4 at 5
No. 449 exposure increased to 2.0 in day 4 at 5
No. 463 exposure increased to 2.0 in day 4 at 5
No. 466 exposure increased to 1.0 in day 4 at 5
No. 470 exposure increased to 2.0 in day 4 at 5
No. 477 exposure increased to 2.0 in day 4 at 5
No. 481 exposure increased to 2.0 in day 4 at 5
No. 508 exposure increased to 4.0 in day 4 at 5
No. 515 exposure increased to 2.0 in day 4 at 5
No. 541 exposure increased to 2.0 in day 4 at 5
No. 551 exposure increased to 2.0 in day 4 at 5
No. 562 exposure increased to 1.0 in day 4 at 5
No. 565 exposure increased to 2.0 in day 4 at 5
No. 570 exposure increased to 3.0 in day 4 at 5
No. 573 exposure increased to 3.0 in day 4 at 5
No. 581 exposure increased to 2.0 in day 4 at 5
No. 584 exposure increased to 2.0 in day 4 at 5
No. 591 exposure increased to 1.0 in day 4 at 5
No. 604 exposure increased to 2.0 in day 4 at 5
No. 672 exposure increased to 1.0 in day 4 at 5
No. 679 exposure increased to 1.0 in day 4 at 5
No. 695 exposure increased to 2.0 in day 4 at 5
No. 704 exposure increased to 1.0 in day 4 at 5
No. 720 exposure increased to 2.0 in day 4 at 5
No. 721 exposure increased to 2.0 in day 4 at 5
No. 727 exposure increased to 2.0 in day 4 at 5
No. 732 exposure increased to 1.0 in day 4 at 5
No. 736 exposure increased to 2.0 in day 4 at 5
No. 741 exposure increased to 1.0 in day 4 at 5
No. 763 exposure increased to 2.0 in day 4 at 5
No. 784 exposure increased to 1.0 in day 4 at 5
No. 792 exposure increased to 2.0 in day 4 at 5
No. 793 exposure increased to 1.0 in day 4 at 5
No. 794 exposure increased to 1.0 in day 4 at 5
No. 797 exposure increased to 1.0 in day 4 at 5
No. 807 exposure increased to 2.0 in day 4 at 5
No. 819 exposure increased to 2.0 in day 4 at 5
No. 821 exposure increased to 2.0 in day 4 at 5
No. 824 exposure increased to 2.0 in day 4 at 5
No. 826 exposure increased to 2.0 in day 4 at 5
*When No. 834 infected, Exposure is 2.0 in day 4 at move 5
No. 838 exposure increased to 1.0 in day 4 at 5
No. 847 exposure increased to 2.0 in day 4 at 5
No. 854 exposure increased to 1.0 in day 4 at 5
No. 861 exposure increased to 1.0 in day 4 at 5
No. 873 exposure increased to 2.0 in day 4 at 5
No. 876 exposure increased to 1.0 in day 4 at 5
No. 880 exposure increased to 2.0 in day 4 at 5
No. 895 exposure increased to 3.0 in day 4 at 5
No. 901 exposure increased to 2.0 in day 4 at 5
No. 923 exposure increased to 2.0 in day 4 at 5
No. 927 exposure increased to 3.0 in day 4 at 5
No. 968 exposure increased to 2.0 in day 4 at 5
No. 969 exposure increased to 2.0 in day 4 at 5
No. 981 exposure increased to 1.0 in day 4 at 5
*When No. 988 infected, Exposure is 2.0 in day 4 at move 5
No. 994 exposure increased to 1.0 in day 4 at 5
  123/10000 [..............................] - ETA: 16:19:53 - reward: 720.4410*When No. 92 infected, Exposure is 2.0 in day 4 at move 0
*When No. 449 infected, Exposure is 2.0 in day 4 at move 0
*When No. 463 infected, Exposure is 2.0 in day 4 at move 0
*When No. 515 infected, Exposure is 2.0 in day 4 at move 0
*When No. 573 infected, Exposure is 3.0 in day 4 at move 0
*When No. 581 infected, Exposure is 2.0 in day 4 at move 0
*When No. 792 infected, Exposure is 2.0 in day 4 at move 0
*When No. 847 infected, Exposure is 2.0 in day 4 at move 0
*When No. 179 infected, Exposure is 2.0 in day 4 at move 1
*When No. 210 infected, Exposure is 4.0 in day 4 at move 1
*When No. 551 infected, Exposure is 2.0 in day 4 at move 1
*When No. 880 infected, Exposure is 2.0 in day 4 at move 1
*When No. 565 infected, Exposure is 2.0 in day 4 at move 2
*When No. 604 infected, Exposure is 2.0 in day 4 at move 2
*When No. 901 infected, Exposure is 2.0 in day 4 at move 2
*When No. 720 infected, Exposure is 2.0 in day 4 at move 3
*When No. 826 infected, Exposure is 2.0 in day 4 at move 3
*When No. 306 infected, Exposure is 2.0 in day 4 at move 4
*When No. 312 infected, Exposure is 2.0 in day 4 at move 4
*When No. 819 infected, Exposure is 2.0 in day 4 at move 4
No. 11 exposure increased to 3.0 in day 4 at 5
No. 13 exposure increased to 4.0 in day 4 at 5
No. 37 exposure increased to 1.0 in day 4 at 5
No. 41 exposure increased to 1.0 in day 4 at 5
No. 54 exposure increased to 2.0 in day 4 at 5
No. 62 exposure increased to 2.0 in day 4 at 5
No. 67 exposure increased to 1.0 in day 4 at 5
No. 68 exposure increased to 2.0 in day 4 at 5
No. 69 exposure increased to 2.0 in day 4 at 5
No. 94 exposure increased to 1.0 in day 4 at 5
*When No. 105 infected, Exposure is 2.0 in day 4 at move 5
No. 107 exposure increased to 3.0 in day 4 at 5
No. 120 exposure increased to 2.0 in day 4 at 5
No. 145 exposure increased to 2.0 in day 4 at 5
No. 156 exposure increased to 1.0 in day 4 at 5
No. 166 exposure increased to 2.0 in day 4 at 5
No. 175 exposure increased to 2.0 in day 4 at 5
No. 183 exposure increased to 2.0 in day 4 at 5
No. 201 exposure increased to 3.0 in day 4 at 5
No. 220 exposure increased to 2.0 in day 4 at 5
No. 221 exposure increased to 1.0 in day 4 at 5
No. 226 exposure increased to 3.0 in day 4 at 5
No. 228 exposure increased to 3.0 in day 4 at 5
No. 231 exposure increased to 3.0 in day 4 at 5
No. 255 exposure increased to 1.0 in day 4 at 5
No. 265 exposure increased to 3.0 in day 4 at 5
No. 279 exposure increased to 2.0 in day 4 at 5
No. 299 exposure increased to 3.0 in day 4 at 5
No. 314 exposure increased to 3.0 in day 4 at 5
No. 316 exposure increased to 3.0 in day 4 at 5
No. 317 exposure increased to 2.0 in day 4 at 5
No. 355 exposure increased to 2.0 in day 4 at 5
No. 374 exposure increased to 1.0 in day 4 at 5
No. 388 exposure increased to 4.0 in day 4 at 5
No. 394 exposure increased to 2.0 in day 4 at 5
*When No. 406 infected, Exposure is 2.0 in day 4 at move 5
No. 419 exposure increased to 2.0 in day 4 at 5
No. 426 exposure increased to 2.0 in day 4 at 5
No. 428 exposure increased to 3.0 in day 4 at 5
No. 439 exposure increased to 2.0 in day 4 at 5
No. 459 exposure increased to 1.0 in day 4 at 5
No. 466 exposure increased to 2.0 in day 4 at 5
No. 470 exposure increased to 3.0 in day 4 at 5
No. 477 exposure increased to 3.0 in day 4 at 5
No. 481 exposure increased to 3.0 in day 4 at 5
No. 506 exposure increased to 1.0 in day 4 at 5
No. 507 exposure increased to 1.0 in day 4 at 5
No. 508 exposure increased to 5.0 in day 4 at 5
*When No. 541 infected, Exposure is 2.0 in day 4 at move 5
No. 562 exposure increased to 2.0 in day 4 at 5
No. 570 exposure increased to 4.0 in day 4 at 5
No. 580 exposure increased to 2.0 in day 4 at 5
No. 584 exposure increased to 3.0 in day 4 at 5
No. 591 exposure increased to 2.0 in day 4 at 5
No. 600 exposure increased to 1.0 in day 4 at 5
No. 622 exposure increased to 1.0 in day 4 at 5
No. 672 exposure increased to 2.0 in day 4 at 5
No. 679 exposure increased to 2.0 in day 4 at 5
No. 695 exposure increased to 3.0 in day 4 at 5
No. 704 exposure increased to 2.0 in day 4 at 5
No. 721 exposure increased to 3.0 in day 4 at 5
No. 723 exposure increased to 2.0 in day 4 at 5
No. 727 exposure increased to 3.0 in day 4 at 5
No. 732 exposure increased to 2.0 in day 4 at 5
*When No. 736 infected, Exposure is 2.0 in day 4 at move 5
No. 741 exposure increased to 2.0 in day 4 at 5
No. 763 exposure increased to 3.0 in day 4 at 5
No. 768 exposure increased to 1.0 in day 4 at 5
No. 773 exposure increased to 1.0 in day 4 at 5
No. 782 exposure increased to 2.0 in day 4 at 5
No. 784 exposure increased to 2.0 in day 4 at 5
No. 785 exposure increased to 1.0 in day 4 at 5
No. 793 exposure increased to 2.0 in day 4 at 5
No. 794 exposure increased to 2.0 in day 4 at 5
No. 797 exposure increased to 2.0 in day 4 at 5
No. 807 exposure increased to 3.0 in day 4 at 5
No. 821 exposure increased to 3.0 in day 4 at 5
No. 824 exposure increased to 3.0 in day 4 at 5
No. 838 exposure increased to 2.0 in day 4 at 5
No. 850 exposure increased to 1.0 in day 4 at 5
No. 854 exposure increased to 2.0 in day 4 at 5
No. 856 exposure increased to 2.0 in day 4 at 5
No. 861 exposure increased to 2.0 in day 4 at 5
No. 873 exposure increased to 3.0 in day 4 at 5
No. 875 exposure increased to 1.0 in day 4 at 5
No. 876 exposure increased to 2.0 in day 4 at 5
No. 895 exposure increased to 4.0 in day 4 at 5
No. 923 exposure increased to 3.0 in day 4 at 5
No. 927 exposure increased to 4.0 in day 4 at 5
No. 937 exposure increased to 2.0 in day 4 at 5
No. 942 exposure increased to 1.0 in day 4 at 5
No. 963 exposure increased to 1.0 in day 4 at 5
No. 968 exposure increased to 3.0 in day 4 at 5
No. 969 exposure increased to 3.0 in day 4 at 5
No. 981 exposure increased to 2.0 in day 4 at 5
No. 994 exposure increased to 2.0 in day 4 at 5
  124/10000 [..............................] - ETA: 16:32:47 - reward: 719.7485*When No. 13 infected, Exposure is 4.0 in day 4 at move 0
*When No. 68 infected, Exposure is 2.0 in day 4 at move 0
*When No. 166 infected, Exposure is 2.0 in day 4 at move 0
*When No. 299 infected, Exposure is 3.0 in day 4 at move 0
*When No. 314 infected, Exposure is 3.0 in day 4 at move 0
*When No. 470 infected, Exposure is 3.0 in day 4 at move 0
*When No. 477 infected, Exposure is 3.0 in day 4 at move 0
*When No. 570 infected, Exposure is 4.0 in day 4 at move 0
*When No. 821 infected, Exposure is 3.0 in day 4 at move 0
*When No. 824 infected, Exposure is 3.0 in day 4 at move 0
*When No. 981 infected, Exposure is 2.0 in day 4 at move 0
*When No. 11 infected, Exposure is 3.0 in day 4 at move 1
*When No. 107 infected, Exposure is 3.0 in day 4 at move 1
*When No. 228 infected, Exposure is 3.0 in day 4 at move 1
*When No. 388 infected, Exposure is 4.0 in day 4 at move 1
*When No. 481 infected, Exposure is 3.0 in day 4 at move 1
*When No. 508 infected, Exposure is 5.0 in day 4 at move 1
*When No. 580 infected, Exposure is 2.0 in day 4 at move 1
*When No. 672 infected, Exposure is 2.0 in day 4 at move 1
*When No. 679 infected, Exposure is 2.0 in day 4 at move 1
*When No. 721 infected, Exposure is 3.0 in day 4 at move 1
*When No. 732 infected, Exposure is 2.0 in day 4 at move 1
*When No. 317 infected, Exposure is 2.0 in day 4 at move 2
*When No. 419 infected, Exposure is 2.0 in day 4 at move 2
*When No. 439 infected, Exposure is 2.0 in day 4 at move 2
*When No. 591 infected, Exposure is 2.0 in day 4 at move 2
*When No. 763 infected, Exposure is 3.0 in day 4 at move 2
*When No. 838 infected, Exposure is 2.0 in day 4 at move 2
*When No. 62 infected, Exposure is 2.0 in day 4 at move 3
*When No. 226 infected, Exposure is 3.0 in day 4 at move 3
*When No. 279 infected, Exposure is 2.0 in day 4 at move 3
*When No. 355 infected, Exposure is 2.0 in day 4 at move 3
*When No. 695 infected, Exposure is 3.0 in day 4 at move 3
*When No. 794 infected, Exposure is 2.0 in day 4 at move 3
*When No. 923 infected, Exposure is 3.0 in day 4 at move 3
*When No. 231 infected, Exposure is 3.0 in day 4 at move 4
*When No. 584 infected, Exposure is 3.0 in day 4 at move 4
*When No. 727 infected, Exposure is 3.0 in day 4 at move 4
No. 4 exposure increased to 2.0 in day 4 at 5
No. 5 exposure increased to 1.0 in day 4 at 5
No. 37 exposure increased to 2.0 in day 4 at 5
No. 41 exposure increased to 2.0 in day 4 at 5
No. 54 exposure increased to 3.0 in day 4 at 5
No. 67 exposure increased to 2.0 in day 4 at 5
No. 69 exposure increased to 3.0 in day 4 at 5
No. 71 exposure increased to 1.0 in day 4 at 5
No. 83 exposure increased to 2.0 in day 4 at 5
No. 87 exposure increased to 1.0 in day 4 at 5
No. 94 exposure increased to 2.0 in day 4 at 5
No. 104 exposure increased to 2.0 in day 4 at 5
No. 120 exposure increased to 3.0 in day 4 at 5
No. 145 exposure increased to 3.0 in day 4 at 5
No. 148 exposure increased to 1.0 in day 4 at 5
No. 156 exposure increased to 2.0 in day 4 at 5
No. 175 exposure increased to 3.0 in day 4 at 5
No. 180 exposure increased to 1.0 in day 4 at 5
No. 183 exposure increased to 3.0 in day 4 at 5
No. 196 exposure increased to 1.0 in day 4 at 5
No. 201 exposure increased to 4.0 in day 4 at 5
No. 214 exposure increased to 1.0 in day 4 at 5
No. 220 exposure increased to 3.0 in day 4 at 5
No. 221 exposure increased to 2.0 in day 4 at 5
No. 244 exposure increased to 2.0 in day 4 at 5
No. 255 exposure increased to 2.0 in day 4 at 5
No. 265 exposure increased to 4.0 in day 4 at 5
No. 269 exposure increased to 2.0 in day 4 at 5
No. 289 exposure increased to 2.0 in day 4 at 5
No. 309 exposure increased to 2.0 in day 4 at 5
No. 316 exposure increased to 4.0 in day 4 at 5
No. 339 exposure increased to 1.0 in day 4 at 5
No. 374 exposure increased to 2.0 in day 4 at 5
No. 382 exposure increased to 1.0 in day 4 at 5
No. 394 exposure increased to 3.0 in day 4 at 5
No. 426 exposure increased to 3.0 in day 4 at 5
No. 428 exposure increased to 4.0 in day 4 at 5
No. 459 exposure increased to 2.0 in day 4 at 5
No. 466 exposure increased to 3.0 in day 4 at 5
No. 503 exposure increased to 1.0 in day 4 at 5
No. 506 exposure increased to 2.0 in day 4 at 5
No. 507 exposure increased to 2.0 in day 4 at 5
No. 522 exposure increased to 1.0 in day 4 at 5
No. 527 exposure increased to 1.0 in day 4 at 5
No. 562 exposure increased to 3.0 in day 4 at 5
No. 600 exposure increased to 2.0 in day 4 at 5
No. 622 exposure increased to 2.0 in day 4 at 5
No. 657 exposure increased to 2.0 in day 4 at 5
No. 660 exposure increased to 2.0 in day 4 at 5
No. 661 exposure increased to 1.0 in day 4 at 5
No. 666 exposure increased to 1.0 in day 4 at 5
No. 700 exposure increased to 1.0 in day 4 at 5
No. 704 exposure increased to 3.0 in day 4 at 5
No. 723 exposure increased to 3.0 in day 4 at 5
No. 730 exposure increased to 1.0 in day 4 at 5
No. 739 exposure increased to 1.0 in day 4 at 5
No. 741 exposure increased to 3.0 in day 4 at 5
No. 745 exposure increased to 1.0 in day 4 at 5
No. 747 exposure increased to 1.0 in day 4 at 5
No. 765 exposure increased to 1.0 in day 4 at 5
No. 768 exposure increased to 2.0 in day 4 at 5
No. 773 exposure increased to 2.0 in day 4 at 5
No. 782 exposure increased to 3.0 in day 4 at 5
No. 784 exposure increased to 3.0 in day 4 at 5
No. 785 exposure increased to 2.0 in day 4 at 5
No. 793 exposure increased to 3.0 in day 4 at 5
No. 797 exposure increased to 3.0 in day 4 at 5
No. 805 exposure increased to 1.0 in day 4 at 5
No. 807 exposure increased to 4.0 in day 4 at 5
No. 809 exposure increased to 1.0 in day 4 at 5
No. 848 exposure increased to 1.0 in day 4 at 5
No. 850 exposure increased to 2.0 in day 4 at 5
No. 854 exposure increased to 3.0 in day 4 at 5
No. 856 exposure increased to 3.0 in day 4 at 5
No. 861 exposure increased to 3.0 in day 4 at 5
*When No. 873 infected, Exposure is 3.0 in day 4 at move 5
No. 875 exposure increased to 2.0 in day 4 at 5
*When No. 876 infected, Exposure is 2.0 in day 4 at move 5
No. 877 exposure increased to 1.0 in day 4 at 5
No. 892 exposure increased to 2.0 in day 4 at 5
No. 895 exposure increased to 5.0 in day 4 at 5
No. 924 exposure increased to 2.0 in day 4 at 5
*When No. 927 infected, Exposure is 4.0 in day 4 at move 5
No. 937 exposure increased to 3.0 in day 4 at 5
No. 942 exposure increased to 2.0 in day 4 at 5
No. 963 exposure increased to 2.0 in day 4 at 5
No. 968 exposure increased to 4.0 in day 4 at 5
No. 969 exposure increased to 4.0 in day 4 at 5
No. 971 exposure increased to 1.0 in day 4 at 5
No. 994 exposure increased to 3.0 in day 4 at 5
  125/10000 [..............................] - ETA: 16:45:31 - reward: 719.3365*When No. 4 infected, Exposure is 2.0 in day 4 at move 0
*When No. 37 infected, Exposure is 2.0 in day 4 at move 0
*When No. 221 infected, Exposure is 2.0 in day 4 at move 0
*When No. 265 infected, Exposure is 4.0 in day 4 at move 0
*When No. 428 infected, Exposure is 4.0 in day 4 at move 0
*When No. 459 infected, Exposure is 2.0 in day 4 at move 0
*When No. 562 infected, Exposure is 3.0 in day 4 at move 0
*When No. 784 infected, Exposure is 3.0 in day 4 at move 0
*When No. 807 infected, Exposure is 4.0 in day 4 at move 0
*When No. 856 infected, Exposure is 3.0 in day 4 at move 0
*When No. 924 infected, Exposure is 2.0 in day 4 at move 0
*When No. 968 infected, Exposure is 4.0 in day 4 at move 0
No. 5 exposure increased to 2.0 in day 4 at 1
No. 41 exposure increased to 3.0 in day 4 at 1
No. 54 exposure increased to 4.0 in day 4 at 1
No. 67 exposure increased to 3.0 in day 4 at 1
*When No. 69 infected, Exposure is 3.0 in day 4 at move 1
No. 71 exposure increased to 2.0 in day 4 at 1
No. 83 exposure increased to 3.0 in day 4 at 1
No. 87 exposure increased to 2.0 in day 4 at 1
No. 94 exposure increased to 3.0 in day 4 at 1
No. 104 exposure increased to 3.0 in day 4 at 1
No. 120 exposure increased to 4.0 in day 4 at 1
No. 124 exposure increased to 1.0 in day 4 at 1
No. 145 exposure increased to 4.0 in day 4 at 1
No. 148 exposure increased to 2.0 in day 4 at 1
No. 155 exposure increased to 1.0 in day 4 at 1
No. 156 exposure increased to 3.0 in day 4 at 1
No. 164 exposure increased to 2.0 in day 4 at 1
No. 175 exposure increased to 4.0 in day 4 at 1
No. 180 exposure increased to 2.0 in day 4 at 1
No. 183 exposure increased to 4.0 in day 4 at 1
No. 192 exposure increased to 2.0 in day 4 at 1
No. 196 exposure increased to 2.0 in day 4 at 1
No. 201 exposure increased to 5.0 in day 4 at 1
No. 214 exposure increased to 2.0 in day 4 at 1
No. 220 exposure increased to 4.0 in day 4 at 1
No. 244 exposure increased to 3.0 in day 4 at 1
No. 255 exposure increased to 3.0 in day 4 at 1
No. 269 exposure increased to 3.0 in day 4 at 1
No. 289 exposure increased to 3.0 in day 4 at 1
No. 309 exposure increased to 3.0 in day 4 at 1
No. 316 exposure increased to 5.0 in day 4 at 1
No. 339 exposure increased to 2.0 in day 4 at 1
No. 374 exposure increased to 3.0 in day 4 at 1
No. 382 exposure increased to 2.0 in day 4 at 1
No. 394 exposure increased to 4.0 in day 4 at 1
No. 414 exposure increased to 2.0 in day 4 at 1
*When No. 426 infected, Exposure is 3.0 in day 4 at move 1
No. 466 exposure increased to 4.0 in day 4 at 1
No. 503 exposure increased to 2.0 in day 4 at 1
No. 506 exposure increased to 3.0 in day 4 at 1
No. 507 exposure increased to 3.0 in day 4 at 1
No. 522 exposure increased to 2.0 in day 4 at 1
No. 527 exposure increased to 2.0 in day 4 at 1
No. 579 exposure increased to 1.0 in day 4 at 1
No. 600 exposure increased to 3.0 in day 4 at 1
No. 622 exposure increased to 3.0 in day 4 at 1
No. 657 exposure increased to 3.0 in day 4 at 1
No. 660 exposure increased to 3.0 in day 4 at 1
No. 661 exposure increased to 2.0 in day 4 at 1
No. 662 exposure increased to 1.0 in day 4 at 1
No. 666 exposure increased to 2.0 in day 4 at 1
No. 681 exposure increased to 1.0 in day 4 at 1
No. 700 exposure increased to 2.0 in day 4 at 1
No. 704 exposure increased to 4.0 in day 4 at 1
*When No. 723 infected, Exposure is 3.0 in day 4 at move 1
No. 730 exposure increased to 2.0 in day 4 at 1
No. 739 exposure increased to 2.0 in day 4 at 1
*When No. 741 infected, Exposure is 3.0 in day 4 at move 1
No. 745 exposure increased to 2.0 in day 4 at 1
No. 747 exposure increased to 2.0 in day 4 at 1
No. 765 exposure increased to 2.0 in day 4 at 1
No. 768 exposure increased to 3.0 in day 4 at 1
*When No. 773 infected, Exposure is 2.0 in day 4 at move 1
No. 782 exposure increased to 4.0 in day 4 at 1
No. 785 exposure increased to 3.0 in day 4 at 1
No. 793 exposure increased to 4.0 in day 4 at 1
No. 797 exposure increased to 4.0 in day 4 at 1
No. 805 exposure increased to 2.0 in day 4 at 1
No. 809 exposure increased to 2.0 in day 4 at 1
No. 848 exposure increased to 2.0 in day 4 at 1
No. 850 exposure increased to 3.0 in day 4 at 1
No. 854 exposure increased to 4.0 in day 4 at 1
No. 861 exposure increased to 4.0 in day 4 at 1
No. 865 exposure increased to 2.0 in day 4 at 1
No. 868 exposure increased to 2.0 in day 4 at 1
*When No. 875 infected, Exposure is 2.0 in day 4 at move 1
No. 877 exposure increased to 2.0 in day 4 at 1
No. 892 exposure increased to 3.0 in day 4 at 1
No. 895 exposure increased to 6.0 in day 4 at 1
No. 918 exposure increased to 1.0 in day 4 at 1
No. 937 exposure increased to 4.0 in day 4 at 1
No. 942 exposure increased to 3.0 in day 4 at 1
*When No. 963 infected, Exposure is 2.0 in day 4 at move 1
*When No. 969 infected, Exposure is 4.0 in day 4 at move 1
No. 971 exposure increased to 2.0 in day 4 at 1
*When No. 994 infected, Exposure is 3.0 in day 4 at move 1
  126/10000 [..............................] - ETA: 16:44:16 - reward: 718.3275*When No. 145 infected, Exposure is 4.0 in day 4 at move 0
*When No. 183 infected, Exposure is 4.0 in day 4 at move 0
*When No. 220 infected, Exposure is 4.0 in day 4 at move 0
*When No. 255 infected, Exposure is 3.0 in day 4 at move 0
*When No. 374 infected, Exposure is 3.0 in day 4 at move 0
*When No. 622 infected, Exposure is 3.0 in day 4 at move 0
*When No. 704 infected, Exposure is 4.0 in day 4 at move 0
*When No. 782 infected, Exposure is 4.0 in day 4 at move 0
*When No. 793 infected, Exposure is 4.0 in day 4 at move 0
*When No. 971 infected, Exposure is 2.0 in day 4 at move 0
*When No. 41 infected, Exposure is 3.0 in day 4 at move 1
*When No. 120 infected, Exposure is 4.0 in day 4 at move 1
*When No. 164 infected, Exposure is 2.0 in day 4 at move 1
*When No. 309 infected, Exposure is 3.0 in day 4 at move 1
*When No. 414 infected, Exposure is 2.0 in day 4 at move 1
*When No. 506 infected, Exposure is 3.0 in day 4 at move 1
*When No. 937 infected, Exposure is 4.0 in day 4 at move 1
*When No. 83 infected, Exposure is 3.0 in day 4 at move 2
*When No. 104 infected, Exposure is 3.0 in day 4 at move 2
*When No. 660 infected, Exposure is 3.0 in day 4 at move 2
*When No. 861 infected, Exposure is 4.0 in day 4 at move 2
*When No. 868 infected, Exposure is 2.0 in day 4 at move 2
*When No. 156 infected, Exposure is 3.0 in day 4 at move 3
*When No. 214 infected, Exposure is 2.0 in day 4 at move 3
*When No. 522 infected, Exposure is 2.0 in day 4 at move 3
*When No. 739 infected, Exposure is 2.0 in day 4 at move 3
*When No. 747 infected, Exposure is 2.0 in day 4 at move 3
*When No. 805 infected, Exposure is 2.0 in day 4 at move 3
*When No. 809 infected, Exposure is 2.0 in day 4 at move 3
*When No. 854 infected, Exposure is 4.0 in day 4 at move 3
*When No. 175 infected, Exposure is 4.0 in day 4 at move 4
*When No. 316 infected, Exposure is 5.0 in day 4 at move 4
*When No. 850 infected, Exposure is 3.0 in day 4 at move 4
*When No. 892 infected, Exposure is 3.0 in day 4 at move 4
*When No. 942 infected, Exposure is 3.0 in day 4 at move 4
No. 5 exposure increased to 3.0 in day 4 at 5
No. 47 exposure increased to 1.0 in day 4 at 5
No. 48 exposure increased to 1.0 in day 4 at 5
No. 53 exposure increased to 1.0 in day 4 at 5
No. 54 exposure increased to 5.0 in day 4 at 5
No. 67 exposure increased to 4.0 in day 4 at 5
No. 71 exposure increased to 3.0 in day 4 at 5
No. 87 exposure increased to 3.0 in day 4 at 5
No. 94 exposure increased to 4.0 in day 4 at 5
No. 122 exposure increased to 1.0 in day 4 at 5
No. 124 exposure increased to 2.0 in day 4 at 5
No. 148 exposure increased to 3.0 in day 4 at 5
No. 150 exposure increased to 2.0 in day 4 at 5
No. 155 exposure increased to 2.0 in day 4 at 5
No. 180 exposure increased to 3.0 in day 4 at 5
No. 182 exposure increased to 1.0 in day 4 at 5
No. 192 exposure increased to 3.0 in day 4 at 5
No. 196 exposure increased to 3.0 in day 4 at 5
No. 201 exposure increased to 6.0 in day 4 at 5
No. 206 exposure increased to 1.0 in day 4 at 5
No. 217 exposure increased to 1.0 in day 4 at 5
No. 222 exposure increased to 2.0 in day 4 at 5
No. 244 exposure increased to 4.0 in day 4 at 5
No. 252 exposure increased to 1.0 in day 4 at 5
No. 269 exposure increased to 4.0 in day 4 at 5
*When No. 289 infected, Exposure is 3.0 in day 4 at move 5
No. 294 exposure increased to 1.0 in day 4 at 5
No. 337 exposure increased to 1.0 in day 4 at 5
No. 339 exposure increased to 3.0 in day 4 at 5
No. 349 exposure increased to 1.0 in day 4 at 5
No. 382 exposure increased to 3.0 in day 4 at 5
No. 394 exposure increased to 5.0 in day 4 at 5
No. 434 exposure increased to 1.0 in day 4 at 5
No. 466 exposure increased to 5.0 in day 4 at 5
No. 474 exposure increased to 1.0 in day 4 at 5
No. 478 exposure increased to 2.0 in day 4 at 5
No. 503 exposure increased to 3.0 in day 4 at 5
No. 507 exposure increased to 4.0 in day 4 at 5
No. 520 exposure increased to 1.0 in day 4 at 5
No. 527 exposure increased to 3.0 in day 4 at 5
No. 579 exposure increased to 2.0 in day 4 at 5
No. 593 exposure increased to 1.0 in day 4 at 5
No. 600 exposure increased to 4.0 in day 4 at 5
No. 626 exposure increased to 1.0 in day 4 at 5
No. 637 exposure increased to 1.0 in day 4 at 5
No. 657 exposure increased to 4.0 in day 4 at 5
No. 661 exposure increased to 3.0 in day 4 at 5
No. 662 exposure increased to 2.0 in day 4 at 5
No. 666 exposure increased to 3.0 in day 4 at 5
No. 681 exposure increased to 2.0 in day 4 at 5
No. 700 exposure increased to 3.0 in day 4 at 5
No. 730 exposure increased to 3.0 in day 4 at 5
No. 737 exposure increased to 1.0 in day 4 at 5
No. 742 exposure increased to 2.0 in day 4 at 5
No. 745 exposure increased to 3.0 in day 4 at 5
*When No. 765 infected, Exposure is 2.0 in day 4 at move 5
No. 768 exposure increased to 4.0 in day 4 at 5
No. 785 exposure increased to 4.0 in day 4 at 5
*When No. 797 infected, Exposure is 4.0 in day 4 at move 5
No. 800 exposure increased to 1.0 in day 4 at 5
No. 802 exposure increased to 1.0 in day 4 at 5
No. 848 exposure increased to 3.0 in day 4 at 5
No. 865 exposure increased to 3.0 in day 4 at 5
No. 877 exposure increased to 3.0 in day 4 at 5
No. 895 exposure increased to 7.0 in day 4 at 5
No. 898 exposure increased to 1.0 in day 4 at 5
No. 918 exposure increased to 2.0 in day 4 at 5
No. 991 exposure increased to 1.0 in day 4 at 5
No. 998 exposure increased to 1.0 in day 4 at 5
  127/10000 [..............................] - ETA: 16:55:42 - reward: 716.8611*When No. 54 infected, Exposure is 5.0 in day 4 at move 0
*When No. 67 infected, Exposure is 4.0 in day 4 at move 0
*When No. 87 infected, Exposure is 3.0 in day 4 at move 0
*When No. 466 infected, Exposure is 5.0 in day 4 at move 0
*When No. 657 infected, Exposure is 4.0 in day 4 at move 0
*When No. 681 infected, Exposure is 2.0 in day 4 at move 0
*When No. 865 infected, Exposure is 3.0 in day 4 at move 0
*When No. 895 infected, Exposure is 7.0 in day 4 at move 0
*When No. 5 infected, Exposure is 3.0 in day 4 at move 1
No. 32 exposure increased to 1.0 in day 4 at 1
No. 47 exposure increased to 2.0 in day 4 at 1
No. 48 exposure increased to 2.0 in day 4 at 1
No. 53 exposure increased to 2.0 in day 4 at 1
No. 71 exposure increased to 4.0 in day 4 at 1
No. 94 exposure increased to 5.0 in day 4 at 1
No. 122 exposure increased to 2.0 in day 4 at 1
No. 124 exposure increased to 3.0 in day 4 at 1
No. 140 exposure increased to 2.0 in day 4 at 1
No. 144 exposure increased to 1.0 in day 4 at 1
No. 148 exposure increased to 4.0 in day 4 at 1
No. 150 exposure increased to 3.0 in day 4 at 1
No. 155 exposure increased to 3.0 in day 4 at 1
No. 180 exposure increased to 4.0 in day 4 at 1
No. 182 exposure increased to 2.0 in day 4 at 1
No. 192 exposure increased to 4.0 in day 4 at 1
No. 196 exposure increased to 4.0 in day 4 at 1
No. 201 exposure increased to 7.0 in day 4 at 1
No. 206 exposure increased to 2.0 in day 4 at 1
No. 217 exposure increased to 2.0 in day 4 at 1
No. 222 exposure increased to 3.0 in day 4 at 1
*When No. 244 infected, Exposure is 4.0 in day 4 at move 1
No. 252 exposure increased to 2.0 in day 4 at 1
No. 269 exposure increased to 5.0 in day 4 at 1
No. 294 exposure increased to 2.0 in day 4 at 1
No. 337 exposure increased to 2.0 in day 4 at 1
No. 339 exposure increased to 4.0 in day 4 at 1
No. 349 exposure increased to 2.0 in day 4 at 1
No. 382 exposure increased to 4.0 in day 4 at 1
No. 394 exposure increased to 6.0 in day 4 at 1
No. 421 exposure increased to 2.0 in day 4 at 1
No. 434 exposure increased to 2.0 in day 4 at 1
No. 451 exposure increased to 2.0 in day 4 at 1
No. 472 exposure increased to 2.0 in day 4 at 1
No. 474 exposure increased to 2.0 in day 4 at 1
No. 478 exposure increased to 3.0 in day 4 at 1
No. 493 exposure increased to 1.0 in day 4 at 1
No. 503 exposure increased to 4.0 in day 4 at 1
*When No. 507 infected, Exposure is 4.0 in day 4 at move 1
No. 520 exposure increased to 2.0 in day 4 at 1
*When No. 527 infected, Exposure is 3.0 in day 4 at move 1
No. 559 exposure increased to 1.0 in day 4 at 1
No. 579 exposure increased to 3.0 in day 4 at 1
No. 593 exposure increased to 2.0 in day 4 at 1
No. 600 exposure increased to 5.0 in day 4 at 1
No. 621 exposure increased to 1.0 in day 4 at 1
No. 626 exposure increased to 2.0 in day 4 at 1
No. 634 exposure increased to 1.0 in day 4 at 1
No. 637 exposure increased to 2.0 in day 4 at 1
No. 661 exposure increased to 4.0 in day 4 at 1
No. 662 exposure increased to 3.0 in day 4 at 1
No. 666 exposure increased to 4.0 in day 4 at 1
No. 700 exposure increased to 4.0 in day 4 at 1
No. 730 exposure increased to 4.0 in day 4 at 1
No. 737 exposure increased to 2.0 in day 4 at 1
No. 742 exposure increased to 3.0 in day 4 at 1
*When No. 745 infected, Exposure is 3.0 in day 4 at move 1
No. 750 exposure increased to 1.0 in day 4 at 1
No. 768 exposure increased to 5.0 in day 4 at 1
No. 785 exposure increased to 5.0 in day 4 at 1
No. 800 exposure increased to 2.0 in day 4 at 1
No. 802 exposure increased to 2.0 in day 4 at 1
No. 823 exposure increased to 1.0 in day 4 at 1
No. 848 exposure increased to 4.0 in day 4 at 1
No. 877 exposure increased to 4.0 in day 4 at 1
No. 898 exposure increased to 2.0 in day 4 at 1
*When No. 918 infected, Exposure is 2.0 in day 4 at move 1
No. 991 exposure increased to 2.0 in day 4 at 1
No. 998 exposure increased to 2.0 in day 4 at 1
  128/10000 [..............................] - ETA: 16:54:11 - reward: 715.8656*When No. 94 infected, Exposure is 5.0 in day 4 at move 0
*When No. 124 infected, Exposure is 3.0 in day 4 at move 0
*When No. 192 infected, Exposure is 4.0 in day 4 at move 0
*When No. 201 infected, Exposure is 7.0 in day 4 at move 0
*When No. 269 infected, Exposure is 5.0 in day 4 at move 0
*When No. 382 infected, Exposure is 4.0 in day 4 at move 0
*When No. 503 infected, Exposure is 4.0 in day 4 at move 0
*When No. 579 infected, Exposure is 3.0 in day 4 at move 0
*When No. 742 infected, Exposure is 3.0 in day 4 at move 0
*When No. 991 infected, Exposure is 2.0 in day 4 at move 0
No. 32 exposure increased to 2.0 in day 4 at 1
No. 47 exposure increased to 3.0 in day 4 at 1
No. 48 exposure increased to 3.0 in day 4 at 1
No. 53 exposure increased to 3.0 in day 4 at 1
No. 71 exposure increased to 5.0 in day 4 at 1
*When No. 122 infected, Exposure is 2.0 in day 4 at move 1
No. 140 exposure increased to 3.0 in day 4 at 1
No. 144 exposure increased to 2.0 in day 4 at 1
No. 148 exposure increased to 5.0 in day 4 at 1
No. 150 exposure increased to 4.0 in day 4 at 1
*When No. 155 infected, Exposure is 3.0 in day 4 at move 1
No. 180 exposure increased to 5.0 in day 4 at 1
No. 182 exposure increased to 3.0 in day 4 at 1
*When No. 196 infected, Exposure is 4.0 in day 4 at move 1
No. 206 exposure increased to 3.0 in day 4 at 1
No. 217 exposure increased to 3.0 in day 4 at 1
No. 222 exposure increased to 4.0 in day 4 at 1
No. 252 exposure increased to 3.0 in day 4 at 1
No. 294 exposure increased to 3.0 in day 4 at 1
No. 296 exposure increased to 1.0 in day 4 at 1
No. 334 exposure increased to 2.0 in day 4 at 1
No. 337 exposure increased to 3.0 in day 4 at 1
No. 339 exposure increased to 5.0 in day 4 at 1
No. 349 exposure increased to 3.0 in day 4 at 1
*When No. 394 infected, Exposure is 6.0 in day 4 at move 1
No. 421 exposure increased to 3.0 in day 4 at 1
No. 434 exposure increased to 3.0 in day 4 at 1
No. 451 exposure increased to 3.0 in day 4 at 1
No. 472 exposure increased to 3.0 in day 4 at 1
No. 474 exposure increased to 3.0 in day 4 at 1
No. 478 exposure increased to 4.0 in day 4 at 1
No. 493 exposure increased to 2.0 in day 4 at 1
No. 520 exposure increased to 3.0 in day 4 at 1
No. 555 exposure increased to 1.0 in day 4 at 1
No. 559 exposure increased to 2.0 in day 4 at 1
No. 593 exposure increased to 3.0 in day 4 at 1
*When No. 600 infected, Exposure is 5.0 in day 4 at move 1
No. 621 exposure increased to 2.0 in day 4 at 1
No. 626 exposure increased to 3.0 in day 4 at 1
No. 634 exposure increased to 2.0 in day 4 at 1
No. 637 exposure increased to 3.0 in day 4 at 1
*When No. 661 infected, Exposure is 4.0 in day 4 at move 1
No. 662 exposure increased to 4.0 in day 4 at 1
No. 666 exposure increased to 5.0 in day 4 at 1
No. 700 exposure increased to 5.0 in day 4 at 1
No. 730 exposure increased to 5.0 in day 4 at 1
No. 737 exposure increased to 3.0 in day 4 at 1
No. 750 exposure increased to 2.0 in day 4 at 1
No. 768 exposure increased to 6.0 in day 4 at 1
No. 785 exposure increased to 6.0 in day 4 at 1
No. 790 exposure increased to 1.0 in day 4 at 1
No. 800 exposure increased to 3.0 in day 4 at 1
*When No. 802 infected, Exposure is 2.0 in day 4 at move 1
No. 814 exposure increased to 2.0 in day 4 at 1
No. 823 exposure increased to 2.0 in day 4 at 1
No. 848 exposure increased to 5.0 in day 4 at 1
*When No. 877 infected, Exposure is 4.0 in day 4 at move 1
*When No. 898 infected, Exposure is 2.0 in day 4 at move 1
No. 911 exposure increased to 1.0 in day 4 at 1
No. 998 exposure increased to 3.0 in day 4 at 1
  129/10000 [..............................] - ETA: 16:52:45 - reward: 714.4744*When No. 150 infected, Exposure is 4.0 in day 4 at move 0
*When No. 180 infected, Exposure is 5.0 in day 4 at move 0
*When No. 206 infected, Exposure is 3.0 in day 4 at move 0
*When No. 294 infected, Exposure is 3.0 in day 4 at move 0
*When No. 339 infected, Exposure is 5.0 in day 4 at move 0
*When No. 785 infected, Exposure is 6.0 in day 4 at move 0
*When No. 848 infected, Exposure is 5.0 in day 4 at move 0
No. 32 exposure increased to 3.0 in day 4 at 1
No. 47 exposure increased to 4.0 in day 4 at 1
No. 48 exposure increased to 4.0 in day 4 at 1
No. 53 exposure increased to 4.0 in day 4 at 1
No. 71 exposure increased to 6.0 in day 4 at 1
No. 96 exposure increased to 1.0 in day 4 at 1
No. 140 exposure increased to 4.0 in day 4 at 1
No. 144 exposure increased to 3.0 in day 4 at 1
No. 148 exposure increased to 6.0 in day 4 at 1
No. 182 exposure increased to 4.0 in day 4 at 1
*When No. 217 infected, Exposure is 3.0 in day 4 at move 1
No. 222 exposure increased to 5.0 in day 4 at 1
No. 249 exposure increased to 2.0 in day 4 at 1
*When No. 252 infected, Exposure is 3.0 in day 4 at move 1
No. 296 exposure increased to 2.0 in day 4 at 1
No. 334 exposure increased to 3.0 in day 4 at 1
No. 337 exposure increased to 4.0 in day 4 at 1
*When No. 349 infected, Exposure is 3.0 in day 4 at move 1
No. 421 exposure increased to 4.0 in day 4 at 1
No. 434 exposure increased to 4.0 in day 4 at 1
No. 451 exposure increased to 4.0 in day 4 at 1
No. 469 exposure increased to 2.0 in day 4 at 1
No. 472 exposure increased to 4.0 in day 4 at 1
No. 474 exposure increased to 4.0 in day 4 at 1
No. 478 exposure increased to 5.0 in day 4 at 1
No. 493 exposure increased to 3.0 in day 4 at 1
No. 520 exposure increased to 4.0 in day 4 at 1
No. 555 exposure increased to 2.0 in day 4 at 1
No. 559 exposure increased to 3.0 in day 4 at 1
No. 593 exposure increased to 4.0 in day 4 at 1
No. 621 exposure increased to 3.0 in day 4 at 1
No. 626 exposure increased to 4.0 in day 4 at 1
No. 634 exposure increased to 3.0 in day 4 at 1
No. 637 exposure increased to 4.0 in day 4 at 1
No. 639 exposure increased to 1.0 in day 4 at 1
No. 650 exposure increased to 1.0 in day 4 at 1
No. 662 exposure increased to 5.0 in day 4 at 1
No. 666 exposure increased to 6.0 in day 4 at 1
No. 667 exposure increased to 1.0 in day 4 at 1
No. 700 exposure increased to 6.0 in day 4 at 1
No. 714 exposure increased to 2.0 in day 4 at 1
*When No. 730 infected, Exposure is 5.0 in day 4 at move 1
No. 737 exposure increased to 4.0 in day 4 at 1
*When No. 750 infected, Exposure is 2.0 in day 4 at move 1
*When No. 768 infected, Exposure is 6.0 in day 4 at move 1
No. 790 exposure increased to 2.0 in day 4 at 1
No. 800 exposure increased to 4.0 in day 4 at 1
*When No. 814 infected, Exposure is 2.0 in day 4 at move 1
No. 823 exposure increased to 3.0 in day 4 at 1
No. 887 exposure increased to 1.0 in day 4 at 1
No. 911 exposure increased to 2.0 in day 4 at 1
No. 998 exposure increased to 4.0 in day 4 at 1
  130/10000 [..............................] - ETA: 16:50:50 - reward: 713.4411*When No. 32 infected, Exposure is 3.0 in day 4 at move 0
*When No. 48 infected, Exposure is 4.0 in day 4 at move 0
*When No. 421 infected, Exposure is 4.0 in day 4 at move 0
*When No. 451 infected, Exposure is 4.0 in day 4 at move 0
*When No. 593 infected, Exposure is 4.0 in day 4 at move 0
*When No. 626 infected, Exposure is 4.0 in day 4 at move 0
*When No. 662 infected, Exposure is 5.0 in day 4 at move 0
*When No. 790 infected, Exposure is 2.0 in day 4 at move 0
*When No. 911 infected, Exposure is 2.0 in day 4 at move 0
*When No. 434 infected, Exposure is 4.0 in day 4 at move 1
*When No. 493 infected, Exposure is 3.0 in day 4 at move 1
*When No. 520 infected, Exposure is 4.0 in day 4 at move 1
*When No. 634 infected, Exposure is 3.0 in day 4 at move 1
*When No. 637 infected, Exposure is 4.0 in day 4 at move 1
*When No. 998 infected, Exposure is 4.0 in day 4 at move 1
*When No. 71 infected, Exposure is 6.0 in day 4 at move 2
*When No. 478 infected, Exposure is 5.0 in day 4 at move 2
*When No. 737 infected, Exposure is 4.0 in day 4 at move 2
*When No. 148 infected, Exposure is 6.0 in day 4 at move 3
*When No. 182 infected, Exposure is 4.0 in day 4 at move 3
*When No. 337 infected, Exposure is 4.0 in day 4 at move 3
*When No. 472 infected, Exposure is 4.0 in day 4 at move 3
*When No. 474 infected, Exposure is 4.0 in day 4 at move 3
*When No. 621 infected, Exposure is 3.0 in day 4 at move 3
*When No. 666 infected, Exposure is 6.0 in day 4 at move 3
*When No. 700 infected, Exposure is 6.0 in day 4 at move 3
*When No. 800 infected, Exposure is 4.0 in day 4 at move 3
*When No. 53 infected, Exposure is 4.0 in day 4 at move 4
*When No. 140 infected, Exposure is 4.0 in day 4 at move 4
*When No. 555 infected, Exposure is 2.0 in day 4 at move 4
*When No. 559 infected, Exposure is 3.0 in day 4 at move 4
No. 33 exposure increased to 1.0 in day 4 at 5
No. 47 exposure increased to 5.0 in day 4 at 5
No. 96 exposure increased to 2.0 in day 4 at 5
No. 144 exposure increased to 4.0 in day 4 at 5
No. 216 exposure increased to 1.0 in day 4 at 5
*When No. 222 infected, Exposure is 5.0 in day 4 at move 5
No. 249 exposure increased to 3.0 in day 4 at 5
No. 277 exposure increased to 2.0 in day 4 at 5
No. 281 exposure increased to 1.0 in day 4 at 5
No. 282 exposure increased to 1.0 in day 4 at 5
No. 296 exposure increased to 3.0 in day 4 at 5
No. 318 exposure increased to 1.0 in day 4 at 5
No. 334 exposure increased to 4.0 in day 4 at 5
No. 360 exposure increased to 2.0 in day 4 at 5
No. 371 exposure increased to 1.0 in day 4 at 5
No. 469 exposure increased to 3.0 in day 4 at 5
No. 516 exposure increased to 1.0 in day 4 at 5
No. 548 exposure increased to 1.0 in day 4 at 5
No. 560 exposure increased to 1.0 in day 4 at 5
No. 639 exposure increased to 2.0 in day 4 at 5
No. 650 exposure increased to 2.0 in day 4 at 5
No. 667 exposure increased to 2.0 in day 4 at 5
No. 714 exposure increased to 3.0 in day 4 at 5
No. 746 exposure increased to 1.0 in day 4 at 5
No. 780 exposure increased to 1.0 in day 4 at 5
No. 812 exposure increased to 1.0 in day 4 at 5
No. 818 exposure increased to 1.0 in day 4 at 5
No. 823 exposure increased to 4.0 in day 4 at 5
No. 841 exposure increased to 1.0 in day 4 at 5
No. 860 exposure increased to 1.0 in day 4 at 5
No. 887 exposure increased to 2.0 in day 4 at 5
No. 948 exposure increased to 1.0 in day 4 at 5
No. 973 exposure increased to 1.0 in day 4 at 5
  131/10000 [..............................] - ETA: 17:01:32 - reward: 711.9198*When No. 47 infected, Exposure is 5.0 in day 4 at move 1
*When No. 296 infected, Exposure is 3.0 in day 4 at move 1
*When No. 334 infected, Exposure is 4.0 in day 4 at move 1
*When No. 887 infected, Exposure is 2.0 in day 4 at move 1
*When No. 249 infected, Exposure is 3.0 in day 4 at move 2
No. 33 exposure increased to 2.0 in day 4 at 5
No. 39 exposure increased to 1.0 in day 4 at 5
No. 56 exposure increased to 1.0 in day 4 at 5
No. 96 exposure increased to 3.0 in day 4 at 5
*When No. 144 infected, Exposure is 4.0 in day 4 at move 5
No. 216 exposure increased to 2.0 in day 4 at 5
No. 277 exposure increased to 3.0 in day 4 at 5
No. 281 exposure increased to 2.0 in day 4 at 5
No. 282 exposure increased to 2.0 in day 4 at 5
No. 318 exposure increased to 2.0 in day 4 at 5
No. 356 exposure increased to 1.0 in day 4 at 5
No. 360 exposure increased to 3.0 in day 4 at 5
No. 362 exposure increased to 1.0 in day 4 at 5
No. 363 exposure increased to 2.0 in day 4 at 5
No. 365 exposure increased to 2.0 in day 4 at 5
No. 371 exposure increased to 2.0 in day 4 at 5
No. 376 exposure increased to 1.0 in day 4 at 5
No. 397 exposure increased to 1.0 in day 4 at 5
No. 429 exposure increased to 2.0 in day 4 at 5
No. 438 exposure increased to 1.0 in day 4 at 5
No. 458 exposure increased to 1.0 in day 4 at 5
No. 469 exposure increased to 4.0 in day 4 at 5
No. 471 exposure increased to 1.0 in day 4 at 5
No. 487 exposure increased to 1.0 in day 4 at 5
No. 494 exposure increased to 1.0 in day 4 at 5
No. 502 exposure increased to 2.0 in day 4 at 5
No. 509 exposure increased to 1.0 in day 4 at 5
No. 516 exposure increased to 2.0 in day 4 at 5
No. 548 exposure increased to 2.0 in day 4 at 5
No. 560 exposure increased to 2.0 in day 4 at 5
No. 586 exposure increased to 1.0 in day 4 at 5
No. 588 exposure increased to 2.0 in day 4 at 5
No. 624 exposure increased to 1.0 in day 4 at 5
No. 627 exposure increased to 1.0 in day 4 at 5
No. 639 exposure increased to 3.0 in day 4 at 5
No. 650 exposure increased to 3.0 in day 4 at 5
No. 655 exposure increased to 2.0 in day 4 at 5
No. 664 exposure increased to 1.0 in day 4 at 5
No. 667 exposure increased to 3.0 in day 4 at 5
No. 680 exposure increased to 1.0 in day 4 at 5
No. 714 exposure increased to 4.0 in day 4 at 5
No. 735 exposure increased to 1.0 in day 4 at 5
No. 746 exposure increased to 2.0 in day 4 at 5
No. 760 exposure increased to 1.0 in day 4 at 5
No. 767 exposure increased to 2.0 in day 4 at 5
No. 780 exposure increased to 2.0 in day 4 at 5
No. 812 exposure increased to 2.0 in day 4 at 5
No. 815 exposure increased to 2.0 in day 4 at 5
No. 818 exposure increased to 2.0 in day 4 at 5
No. 823 exposure increased to 5.0 in day 4 at 5
No. 825 exposure increased to 1.0 in day 4 at 5
No. 841 exposure increased to 2.0 in day 4 at 5
No. 849 exposure increased to 1.0 in day 4 at 5
No. 860 exposure increased to 2.0 in day 4 at 5
No. 864 exposure increased to 1.0 in day 4 at 5
No. 905 exposure increased to 1.0 in day 4 at 5
No. 915 exposure increased to 1.0 in day 4 at 5
No. 928 exposure increased to 1.0 in day 4 at 5
No. 948 exposure increased to 2.0 in day 4 at 5
No. 973 exposure increased to 2.0 in day 4 at 5
No. 982 exposure increased to 1.0 in day 4 at 5
No. 993 exposure increased to 1.0 in day 4 at 5
  132/10000 [..............................] - ETA: 17:10:15 - reward: 710.6496*When No. 363 infected, Exposure is 2.0 in day 4 at move 0
*When No. 516 infected, Exposure is 2.0 in day 4 at move 0
*When No. 639 infected, Exposure is 3.0 in day 4 at move 0
*When No. 281 infected, Exposure is 2.0 in day 4 at move 1
*When No. 469 infected, Exposure is 4.0 in day 4 at move 1
*When No. 502 infected, Exposure is 2.0 in day 4 at move 1
*When No. 650 infected, Exposure is 3.0 in day 4 at move 1
*When No. 823 infected, Exposure is 5.0 in day 4 at move 1
*When No. 841 infected, Exposure is 2.0 in day 4 at move 1
*When No. 360 infected, Exposure is 3.0 in day 4 at move 2
*When No. 560 infected, Exposure is 2.0 in day 4 at move 2
*When No. 33 infected, Exposure is 2.0 in day 4 at move 3
*When No. 365 infected, Exposure is 2.0 in day 4 at move 3
*When No. 548 infected, Exposure is 2.0 in day 4 at move 4
*When No. 973 infected, Exposure is 2.0 in day 4 at move 4
No. 39 exposure increased to 2.0 in day 4 at 5
No. 56 exposure increased to 2.0 in day 4 at 5
No. 96 exposure increased to 4.0 in day 4 at 5
No. 139 exposure increased to 1.0 in day 4 at 5
No. 146 exposure increased to 1.0 in day 4 at 5
No. 167 exposure increased to 1.0 in day 4 at 5
No. 188 exposure increased to 1.0 in day 4 at 5
*When No. 216 infected, Exposure is 2.0 in day 4 at move 5
No. 257 exposure increased to 1.0 in day 4 at 5
No. 264 exposure increased to 1.0 in day 4 at 5
No. 277 exposure increased to 4.0 in day 4 at 5
No. 282 exposure increased to 3.0 in day 4 at 5
No. 305 exposure increased to 1.0 in day 4 at 5
No. 318 exposure increased to 3.0 in day 4 at 5
No. 356 exposure increased to 2.0 in day 4 at 5
No. 362 exposure increased to 2.0 in day 4 at 5
No. 371 exposure increased to 3.0 in day 4 at 5
No. 376 exposure increased to 2.0 in day 4 at 5
No. 397 exposure increased to 2.0 in day 4 at 5
No. 398 exposure increased to 1.0 in day 4 at 5
No. 423 exposure increased to 1.0 in day 4 at 5
No. 429 exposure increased to 3.0 in day 4 at 5
No. 438 exposure increased to 2.0 in day 4 at 5
No. 440 exposure increased to 1.0 in day 4 at 5
No. 441 exposure increased to 1.0 in day 4 at 5
No. 458 exposure increased to 2.0 in day 4 at 5
No. 471 exposure increased to 2.0 in day 4 at 5
No. 487 exposure increased to 2.0 in day 4 at 5
No. 489 exposure increased to 2.0 in day 4 at 5
No. 494 exposure increased to 2.0 in day 4 at 5
No. 509 exposure increased to 2.0 in day 4 at 5
No. 512 exposure increased to 1.0 in day 4 at 5
No. 531 exposure increased to 1.0 in day 4 at 5
No. 563 exposure increased to 2.0 in day 4 at 5
No. 586 exposure increased to 2.0 in day 4 at 5
No. 588 exposure increased to 3.0 in day 4 at 5
No. 624 exposure increased to 2.0 in day 4 at 5
No. 627 exposure increased to 2.0 in day 4 at 5
No. 630 exposure increased to 1.0 in day 4 at 5
No. 647 exposure increased to 1.0 in day 4 at 5
No. 655 exposure increased to 3.0 in day 4 at 5
No. 664 exposure increased to 2.0 in day 4 at 5
*When No. 667 infected, Exposure is 3.0 in day 4 at move 5
No. 680 exposure increased to 2.0 in day 4 at 5
*When No. 714 infected, Exposure is 4.0 in day 4 at move 5
No. 716 exposure increased to 1.0 in day 4 at 5
No. 735 exposure increased to 2.0 in day 4 at 5
No. 740 exposure increased to 1.0 in day 4 at 5
No. 746 exposure increased to 3.0 in day 4 at 5
No. 748 exposure increased to 2.0 in day 4 at 5
No. 760 exposure increased to 2.0 in day 4 at 5
No. 767 exposure increased to 3.0 in day 4 at 5
No. 769 exposure increased to 2.0 in day 4 at 5
No. 770 exposure increased to 1.0 in day 4 at 5
No. 780 exposure increased to 3.0 in day 4 at 5
No. 812 exposure increased to 3.0 in day 4 at 5
No. 815 exposure increased to 3.0 in day 4 at 5
No. 817 exposure increased to 1.0 in day 4 at 5
No. 818 exposure increased to 3.0 in day 4 at 5
No. 825 exposure increased to 2.0 in day 4 at 5
No. 846 exposure increased to 1.0 in day 4 at 5
No. 849 exposure increased to 2.0 in day 4 at 5
No. 860 exposure increased to 3.0 in day 4 at 5
No. 863 exposure increased to 1.0 in day 4 at 5
No. 864 exposure increased to 2.0 in day 4 at 5
No. 869 exposure increased to 1.0 in day 4 at 5
No. 870 exposure increased to 1.0 in day 4 at 5
No. 894 exposure increased to 1.0 in day 4 at 5
No. 905 exposure increased to 2.0 in day 4 at 5
No. 915 exposure increased to 2.0 in day 4 at 5
No. 928 exposure increased to 2.0 in day 4 at 5
No. 948 exposure increased to 3.0 in day 4 at 5
No. 952 exposure increased to 1.0 in day 4 at 5
No. 954 exposure increased to 1.0 in day 4 at 5
No. 982 exposure increased to 2.0 in day 4 at 5
No. 985 exposure increased to 1.0 in day 4 at 5
No. 993 exposure increased to 2.0 in day 4 at 5
  133/10000 [..............................] - ETA: 17:17:29 - reward: 708.8874*When No. 96 infected, Exposure is 4.0 in day 4 at move 0
*When No. 277 infected, Exposure is 4.0 in day 4 at move 0
*When No. 489 infected, Exposure is 2.0 in day 4 at move 0
*When No. 494 infected, Exposure is 2.0 in day 4 at move 0
*When No. 905 infected, Exposure is 2.0 in day 4 at move 0
*When No. 56 infected, Exposure is 2.0 in day 4 at move 1
*When No. 371 infected, Exposure is 3.0 in day 4 at move 1
*When No. 376 infected, Exposure is 2.0 in day 4 at move 1
*When No. 471 infected, Exposure is 2.0 in day 4 at move 1
*When No. 487 infected, Exposure is 2.0 in day 4 at move 1
*When No. 655 infected, Exposure is 3.0 in day 4 at move 1
*When No. 769 infected, Exposure is 2.0 in day 4 at move 1
*When No. 928 infected, Exposure is 2.0 in day 4 at move 1
*When No. 588 infected, Exposure is 3.0 in day 4 at move 2
*When No. 812 infected, Exposure is 3.0 in day 4 at move 2
*When No. 915 infected, Exposure is 2.0 in day 4 at move 2
*When No. 948 infected, Exposure is 3.0 in day 4 at move 2
*When No. 746 infected, Exposure is 3.0 in day 4 at move 3
*When No. 760 infected, Exposure is 2.0 in day 4 at move 3
*When No. 815 infected, Exposure is 3.0 in day 4 at move 3
*When No. 39 infected, Exposure is 2.0 in day 4 at move 4
*When No. 318 infected, Exposure is 3.0 in day 4 at move 4
*When No. 780 infected, Exposure is 3.0 in day 4 at move 4
No. 42 exposure increased to 1.0 in day 4 at 5
No. 116 exposure increased to 1.0 in day 4 at 5
No. 139 exposure increased to 2.0 in day 4 at 5
No. 146 exposure increased to 2.0 in day 4 at 5
No. 167 exposure increased to 2.0 in day 4 at 5
No. 186 exposure increased to 1.0 in day 4 at 5
No. 188 exposure increased to 2.0 in day 4 at 5
No. 227 exposure increased to 1.0 in day 4 at 5
No. 242 exposure increased to 1.0 in day 4 at 5
No. 248 exposure increased to 1.0 in day 4 at 5
No. 254 exposure increased to 2.0 in day 4 at 5
No. 257 exposure increased to 2.0 in day 4 at 5
No. 264 exposure increased to 2.0 in day 4 at 5
No. 282 exposure increased to 4.0 in day 4 at 5
No. 305 exposure increased to 2.0 in day 4 at 5
No. 333 exposure increased to 1.0 in day 4 at 5
No. 356 exposure increased to 3.0 in day 4 at 5
*When No. 362 infected, Exposure is 2.0 in day 4 at move 5
No. 397 exposure increased to 3.0 in day 4 at 5
No. 398 exposure increased to 2.0 in day 4 at 5
No. 401 exposure increased to 1.0 in day 4 at 5
No. 423 exposure increased to 2.0 in day 4 at 5
No. 429 exposure increased to 4.0 in day 4 at 5
No. 438 exposure increased to 3.0 in day 4 at 5
No. 440 exposure increased to 2.0 in day 4 at 5
No. 441 exposure increased to 2.0 in day 4 at 5
No. 458 exposure increased to 3.0 in day 4 at 5
No. 505 exposure increased to 1.0 in day 4 at 5
No. 509 exposure increased to 3.0 in day 4 at 5
No. 512 exposure increased to 2.0 in day 4 at 5
No. 531 exposure increased to 2.0 in day 4 at 5
No. 563 exposure increased to 3.0 in day 4 at 5
No. 578 exposure increased to 1.0 in day 4 at 5
No. 586 exposure increased to 3.0 in day 4 at 5
No. 594 exposure increased to 1.0 in day 4 at 5
No. 595 exposure increased to 1.0 in day 4 at 5
No. 624 exposure increased to 3.0 in day 4 at 5
No. 627 exposure increased to 3.0 in day 4 at 5
No. 630 exposure increased to 2.0 in day 4 at 5
No. 644 exposure increased to 1.0 in day 4 at 5
No. 647 exposure increased to 2.0 in day 4 at 5
No. 652 exposure increased to 1.0 in day 4 at 5
No. 656 exposure increased to 1.0 in day 4 at 5
No. 664 exposure increased to 3.0 in day 4 at 5
No. 680 exposure increased to 3.0 in day 4 at 5
No. 716 exposure increased to 2.0 in day 4 at 5
No. 717 exposure increased to 1.0 in day 4 at 5
No. 735 exposure increased to 3.0 in day 4 at 5
No. 740 exposure increased to 2.0 in day 4 at 5
No. 748 exposure increased to 3.0 in day 4 at 5
No. 767 exposure increased to 4.0 in day 4 at 5
No. 770 exposure increased to 2.0 in day 4 at 5
No. 789 exposure increased to 1.0 in day 4 at 5
No. 796 exposure increased to 1.0 in day 4 at 5
No. 811 exposure increased to 1.0 in day 4 at 5
No. 817 exposure increased to 2.0 in day 4 at 5
No. 818 exposure increased to 4.0 in day 4 at 5
No. 825 exposure increased to 3.0 in day 4 at 5
No. 827 exposure increased to 1.0 in day 4 at 5
No. 846 exposure increased to 2.0 in day 4 at 5
No. 849 exposure increased to 3.0 in day 4 at 5
*When No. 860 infected, Exposure is 3.0 in day 4 at move 5
No. 863 exposure increased to 2.0 in day 4 at 5
No. 864 exposure increased to 3.0 in day 4 at 5
No. 869 exposure increased to 2.0 in day 4 at 5
No. 870 exposure increased to 2.0 in day 4 at 5
No. 894 exposure increased to 2.0 in day 4 at 5
No. 899 exposure increased to 1.0 in day 4 at 5
No. 902 exposure increased to 1.0 in day 4 at 5
No. 929 exposure increased to 2.0 in day 4 at 5
No. 950 exposure increased to 1.0 in day 4 at 5
No. 952 exposure increased to 2.0 in day 4 at 5
No. 954 exposure increased to 2.0 in day 4 at 5
No. 979 exposure increased to 2.0 in day 4 at 5
No. 982 exposure increased to 3.0 in day 4 at 5
No. 985 exposure increased to 2.0 in day 4 at 5
No. 993 exposure increased to 3.0 in day 4 at 5
  134/10000 [..............................] - ETA: 17:24:15 - reward: 707.4283*When No. 146 infected, Exposure is 2.0 in day 4 at move 0
*When No. 356 infected, Exposure is 3.0 in day 4 at move 0
*When No. 397 infected, Exposure is 3.0 in day 4 at move 0
*When No. 735 infected, Exposure is 3.0 in day 4 at move 0
*When No. 864 infected, Exposure is 3.0 in day 4 at move 0
*When No. 429 infected, Exposure is 4.0 in day 4 at move 1
*When No. 438 infected, Exposure is 3.0 in day 4 at move 1
*When No. 512 infected, Exposure is 2.0 in day 4 at move 1
*When No. 563 infected, Exposure is 3.0 in day 4 at move 1
*When No. 627 infected, Exposure is 3.0 in day 4 at move 1
*When No. 664 infected, Exposure is 3.0 in day 4 at move 1
*When No. 818 infected, Exposure is 4.0 in day 4 at move 1
*When No. 849 infected, Exposure is 3.0 in day 4 at move 1
*When No. 139 infected, Exposure is 2.0 in day 4 at move 2
*When No. 167 infected, Exposure is 2.0 in day 4 at move 2
*When No. 624 infected, Exposure is 3.0 in day 4 at move 2
*When No. 767 infected, Exposure is 4.0 in day 4 at move 2
*When No. 979 infected, Exposure is 2.0 in day 4 at move 2
*When No. 398 infected, Exposure is 2.0 in day 4 at move 3
*When No. 458 infected, Exposure is 3.0 in day 4 at move 3
*When No. 509 infected, Exposure is 3.0 in day 4 at move 3
*When No. 740 infected, Exposure is 2.0 in day 4 at move 3
*When No. 264 infected, Exposure is 2.0 in day 4 at move 4
*When No. 846 infected, Exposure is 2.0 in day 4 at move 4
*When No. 869 infected, Exposure is 2.0 in day 4 at move 4
*When No. 952 infected, Exposure is 2.0 in day 4 at move 4
No. 3 exposure increased to 1.0 in day 4 at 5
No. 42 exposure increased to 2.0 in day 4 at 5
No. 109 exposure increased to 1.0 in day 4 at 5
No. 116 exposure increased to 2.0 in day 4 at 5
No. 125 exposure increased to 1.0 in day 4 at 5
No. 174 exposure increased to 1.0 in day 4 at 5
No. 186 exposure increased to 2.0 in day 4 at 5
No. 188 exposure increased to 3.0 in day 4 at 5
No. 195 exposure increased to 1.0 in day 4 at 5
No. 199 exposure increased to 2.0 in day 4 at 5
No. 209 exposure increased to 2.0 in day 4 at 5
No. 227 exposure increased to 2.0 in day 4 at 5
No. 242 exposure increased to 2.0 in day 4 at 5
No. 248 exposure increased to 2.0 in day 4 at 5
No. 254 exposure increased to 3.0 in day 4 at 5
No. 257 exposure increased to 3.0 in day 4 at 5
*When No. 282 infected, Exposure is 4.0 in day 4 at move 5
No. 305 exposure increased to 3.0 in day 4 at 5
No. 323 exposure increased to 1.0 in day 4 at 5
No. 333 exposure increased to 2.0 in day 4 at 5
No. 367 exposure increased to 1.0 in day 4 at 5
No. 401 exposure increased to 2.0 in day 4 at 5
No. 413 exposure increased to 1.0 in day 4 at 5
*When No. 423 infected, Exposure is 2.0 in day 4 at move 5
No. 427 exposure increased to 2.0 in day 4 at 5
No. 437 exposure increased to 1.0 in day 4 at 5
No. 440 exposure increased to 3.0 in day 4 at 5
No. 441 exposure increased to 3.0 in day 4 at 5
No. 468 exposure increased to 1.0 in day 4 at 5
No. 505 exposure increased to 2.0 in day 4 at 5
No. 531 exposure increased to 3.0 in day 4 at 5
No. 578 exposure increased to 2.0 in day 4 at 5
No. 583 exposure increased to 1.0 in day 4 at 5
No. 586 exposure increased to 4.0 in day 4 at 5
No. 594 exposure increased to 2.0 in day 4 at 5
No. 595 exposure increased to 2.0 in day 4 at 5
No. 602 exposure increased to 1.0 in day 4 at 5
No. 630 exposure increased to 3.0 in day 4 at 5
No. 644 exposure increased to 2.0 in day 4 at 5
No. 646 exposure increased to 1.0 in day 4 at 5
No. 647 exposure increased to 3.0 in day 4 at 5
No. 652 exposure increased to 2.0 in day 4 at 5
No. 656 exposure increased to 2.0 in day 4 at 5
No. 671 exposure increased to 1.0 in day 4 at 5
No. 674 exposure increased to 2.0 in day 4 at 5
No. 680 exposure increased to 4.0 in day 4 at 5
No. 716 exposure increased to 3.0 in day 4 at 5
No. 717 exposure increased to 2.0 in day 4 at 5
No. 748 exposure increased to 4.0 in day 4 at 5
No. 770 exposure increased to 3.0 in day 4 at 5
No. 789 exposure increased to 2.0 in day 4 at 5
No. 796 exposure increased to 2.0 in day 4 at 5
No. 811 exposure increased to 2.0 in day 4 at 5
*When No. 817 infected, Exposure is 2.0 in day 4 at move 5
*When No. 825 infected, Exposure is 3.0 in day 4 at move 5
No. 827 exposure increased to 2.0 in day 4 at 5
No. 863 exposure increased to 3.0 in day 4 at 5
No. 870 exposure increased to 3.0 in day 4 at 5
No. 894 exposure increased to 3.0 in day 4 at 5
No. 899 exposure increased to 2.0 in day 4 at 5
No. 902 exposure increased to 2.0 in day 4 at 5
No. 907 exposure increased to 1.0 in day 4 at 5
No. 912 exposure increased to 2.0 in day 4 at 5
No. 929 exposure increased to 3.0 in day 4 at 5
No. 940 exposure increased to 1.0 in day 4 at 5
No. 950 exposure increased to 2.0 in day 4 at 5
No. 951 exposure increased to 1.0 in day 4 at 5
No. 954 exposure increased to 3.0 in day 4 at 5
No. 957 exposure increased to 2.0 in day 4 at 5
*When No. 982 infected, Exposure is 3.0 in day 4 at move 5
No. 985 exposure increased to 3.0 in day 4 at 5
No. 993 exposure increased to 4.0 in day 4 at 5
No. 996 exposure increased to 1.0 in day 4 at 5
  135/10000 [..............................] - ETA: 17:38:34 - reward: 705.8340*When No. 242 infected, Exposure is 2.0 in day 4 at move 0
*When No. 254 infected, Exposure is 3.0 in day 4 at move 0
*When No. 305 infected, Exposure is 3.0 in day 4 at move 0
*When No. 505 infected, Exposure is 2.0 in day 4 at move 0
*When No. 531 infected, Exposure is 3.0 in day 4 at move 0
*When No. 586 infected, Exposure is 4.0 in day 4 at move 0
*When No. 827 infected, Exposure is 2.0 in day 4 at move 0
*When No. 894 infected, Exposure is 3.0 in day 4 at move 0
*When No. 954 infected, Exposure is 3.0 in day 4 at move 0
No. 3 exposure increased to 2.0 in day 4 at 1
No. 42 exposure increased to 3.0 in day 4 at 1
No. 109 exposure increased to 2.0 in day 4 at 1
No. 116 exposure increased to 3.0 in day 4 at 1
No. 125 exposure increased to 2.0 in day 4 at 1
No. 174 exposure increased to 2.0 in day 4 at 1
No. 186 exposure increased to 3.0 in day 4 at 1
*When No. 188 infected, Exposure is 3.0 in day 4 at move 1
No. 195 exposure increased to 2.0 in day 4 at 1
No. 199 exposure increased to 3.0 in day 4 at 1
No. 209 exposure increased to 3.0 in day 4 at 1
No. 227 exposure increased to 3.0 in day 4 at 1
No. 248 exposure increased to 3.0 in day 4 at 1
No. 257 exposure increased to 4.0 in day 4 at 1
No. 304 exposure increased to 1.0 in day 4 at 1
No. 307 exposure increased to 1.0 in day 4 at 1
No. 313 exposure increased to 2.0 in day 4 at 1
No. 323 exposure increased to 2.0 in day 4 at 1
*When No. 333 infected, Exposure is 2.0 in day 4 at move 1
No. 367 exposure increased to 2.0 in day 4 at 1
No. 401 exposure increased to 3.0 in day 4 at 1
No. 402 exposure increased to 1.0 in day 4 at 1
No. 411 exposure increased to 2.0 in day 4 at 1
No. 413 exposure increased to 2.0 in day 4 at 1
No. 427 exposure increased to 3.0 in day 4 at 1
No. 437 exposure increased to 2.0 in day 4 at 1
No. 440 exposure increased to 4.0 in day 4 at 1
No. 441 exposure increased to 4.0 in day 4 at 1
No. 457 exposure increased to 2.0 in day 4 at 1
No. 468 exposure increased to 2.0 in day 4 at 1
No. 504 exposure increased to 1.0 in day 4 at 1
No. 578 exposure increased to 3.0 in day 4 at 1
No. 583 exposure increased to 2.0 in day 4 at 1
No. 594 exposure increased to 3.0 in day 4 at 1
No. 595 exposure increased to 3.0 in day 4 at 1
No. 602 exposure increased to 2.0 in day 4 at 1
No. 630 exposure increased to 4.0 in day 4 at 1
No. 644 exposure increased to 3.0 in day 4 at 1
No. 646 exposure increased to 2.0 in day 4 at 1
*When No. 647 infected, Exposure is 3.0 in day 4 at move 1
No. 652 exposure increased to 3.0 in day 4 at 1
No. 656 exposure increased to 3.0 in day 4 at 1
No. 671 exposure increased to 2.0 in day 4 at 1
No. 674 exposure increased to 3.0 in day 4 at 1
*When No. 680 infected, Exposure is 4.0 in day 4 at move 1
*When No. 716 infected, Exposure is 3.0 in day 4 at move 1
No. 717 exposure increased to 3.0 in day 4 at 1
*When No. 748 infected, Exposure is 4.0 in day 4 at move 1
No. 770 exposure increased to 4.0 in day 4 at 1
No. 789 exposure increased to 3.0 in day 4 at 1
No. 796 exposure increased to 3.0 in day 4 at 1
No. 806 exposure increased to 1.0 in day 4 at 1
No. 811 exposure increased to 3.0 in day 4 at 1
*When No. 863 infected, Exposure is 3.0 in day 4 at move 1
No. 870 exposure increased to 4.0 in day 4 at 1
No. 899 exposure increased to 3.0 in day 4 at 1
No. 902 exposure increased to 3.0 in day 4 at 1
No. 907 exposure increased to 2.0 in day 4 at 1
No. 912 exposure increased to 3.0 in day 4 at 1
*When No. 929 infected, Exposure is 3.0 in day 4 at move 1
No. 940 exposure increased to 2.0 in day 4 at 1
No. 950 exposure increased to 3.0 in day 4 at 1
No. 951 exposure increased to 2.0 in day 4 at 1
*When No. 957 infected, Exposure is 2.0 in day 4 at move 1
*When No. 985 infected, Exposure is 3.0 in day 4 at move 1
No. 993 exposure increased to 5.0 in day 4 at 1
No. 996 exposure increased to 2.0 in day 4 at 1
  136/10000 [..............................] - ETA: 17:35:22 - reward: 704.3217*When No. 209 infected, Exposure is 3.0 in day 4 at move 0
*When No. 227 infected, Exposure is 3.0 in day 4 at move 0
*When No. 257 infected, Exposure is 4.0 in day 4 at move 0
*When No. 313 infected, Exposure is 2.0 in day 4 at move 0
*When No. 457 infected, Exposure is 2.0 in day 4 at move 0
*When No. 578 infected, Exposure is 3.0 in day 4 at move 0
*When No. 594 infected, Exposure is 3.0 in day 4 at move 0
*When No. 652 infected, Exposure is 3.0 in day 4 at move 0
*When No. 796 infected, Exposure is 3.0 in day 4 at move 0
*When No. 811 infected, Exposure is 3.0 in day 4 at move 0
*When No. 116 infected, Exposure is 3.0 in day 4 at move 1
*When No. 595 infected, Exposure is 3.0 in day 4 at move 1
*When No. 630 infected, Exposure is 4.0 in day 4 at move 1
*When No. 656 infected, Exposure is 3.0 in day 4 at move 1
*When No. 674 infected, Exposure is 3.0 in day 4 at move 1
*When No. 940 infected, Exposure is 2.0 in day 4 at move 1
*When No. 993 infected, Exposure is 5.0 in day 4 at move 1
*When No. 411 infected, Exposure is 2.0 in day 4 at move 2
*When No. 248 infected, Exposure is 3.0 in day 4 at move 3
*When No. 671 infected, Exposure is 2.0 in day 4 at move 3
*When No. 717 infected, Exposure is 3.0 in day 4 at move 3
*When No. 789 infected, Exposure is 3.0 in day 4 at move 3
*When No. 907 infected, Exposure is 2.0 in day 4 at move 3
*When No. 912 infected, Exposure is 3.0 in day 4 at move 3
*When No. 186 infected, Exposure is 3.0 in day 4 at move 4
*When No. 195 infected, Exposure is 2.0 in day 4 at move 4
*When No. 199 infected, Exposure is 3.0 in day 4 at move 4
*When No. 413 infected, Exposure is 2.0 in day 4 at move 4
*When No. 427 infected, Exposure is 3.0 in day 4 at move 4
*When No. 644 infected, Exposure is 3.0 in day 4 at move 4
*When No. 870 infected, Exposure is 4.0 in day 4 at move 4
No. 3 exposure increased to 3.0 in day 4 at 5
No. 38 exposure increased to 1.0 in day 4 at 5
No. 42 exposure increased to 4.0 in day 4 at 5
No. 91 exposure increased to 1.0 in day 4 at 5
No. 103 exposure increased to 1.0 in day 4 at 5
No. 108 exposure increased to 1.0 in day 4 at 5
No. 109 exposure increased to 3.0 in day 4 at 5
No. 125 exposure increased to 3.0 in day 4 at 5
No. 141 exposure increased to 1.0 in day 4 at 5
No. 168 exposure increased to 1.0 in day 4 at 5
No. 174 exposure increased to 3.0 in day 4 at 5
No. 215 exposure increased to 1.0 in day 4 at 5
No. 239 exposure increased to 1.0 in day 4 at 5
No. 303 exposure increased to 2.0 in day 4 at 5
No. 304 exposure increased to 2.0 in day 4 at 5
No. 307 exposure increased to 2.0 in day 4 at 5
No. 323 exposure increased to 3.0 in day 4 at 5
No. 326 exposure increased to 1.0 in day 4 at 5
No. 350 exposure increased to 1.0 in day 4 at 5
No. 367 exposure increased to 3.0 in day 4 at 5
No. 368 exposure increased to 1.0 in day 4 at 5
No. 401 exposure increased to 4.0 in day 4 at 5
No. 402 exposure increased to 2.0 in day 4 at 5
No. 437 exposure increased to 3.0 in day 4 at 5
*When No. 440 infected, Exposure is 4.0 in day 4 at move 5
No. 441 exposure increased to 5.0 in day 4 at 5
No. 468 exposure increased to 3.0 in day 4 at 5
No. 504 exposure increased to 2.0 in day 4 at 5
No. 514 exposure increased to 1.0 in day 4 at 5
No. 519 exposure increased to 1.0 in day 4 at 5
No. 543 exposure increased to 1.0 in day 4 at 5
No. 583 exposure increased to 3.0 in day 4 at 5
No. 587 exposure increased to 1.0 in day 4 at 5
No. 602 exposure increased to 3.0 in day 4 at 5
No. 643 exposure increased to 2.0 in day 4 at 5
No. 646 exposure increased to 3.0 in day 4 at 5
No. 676 exposure increased to 1.0 in day 4 at 5
No. 687 exposure increased to 1.0 in day 4 at 5
No. 691 exposure increased to 1.0 in day 4 at 5
No. 770 exposure increased to 5.0 in day 4 at 5
No. 772 exposure increased to 1.0 in day 4 at 5
No. 806 exposure increased to 2.0 in day 4 at 5
No. 883 exposure increased to 2.0 in day 4 at 5
No. 884 exposure increased to 1.0 in day 4 at 5
No. 899 exposure increased to 4.0 in day 4 at 5
No. 902 exposure increased to 4.0 in day 4 at 5
No. 903 exposure increased to 1.0 in day 4 at 5
No. 921 exposure increased to 1.0 in day 4 at 5
No. 922 exposure increased to 1.0 in day 4 at 5
No. 926 exposure increased to 1.0 in day 4 at 5
No. 931 exposure increased to 1.0 in day 4 at 5
No. 950 exposure increased to 4.0 in day 4 at 5
No. 951 exposure increased to 3.0 in day 4 at 5
No. 987 exposure increased to 1.0 in day 4 at 5
No. 996 exposure increased to 3.0 in day 4 at 5
  137/10000 [..............................] - ETA: 17:42:42 - reward: 702.2826*When No. 3 infected, Exposure is 3.0 in day 4 at move 0
*When No. 42 infected, Exposure is 4.0 in day 4 at move 0
*When No. 303 infected, Exposure is 2.0 in day 4 at move 0
*When No. 323 infected, Exposure is 3.0 in day 4 at move 0
*When No. 367 infected, Exposure is 3.0 in day 4 at move 0
*When No. 401 infected, Exposure is 4.0 in day 4 at move 0
*When No. 402 infected, Exposure is 2.0 in day 4 at move 0
*When No. 437 infected, Exposure is 3.0 in day 4 at move 0
*When No. 583 infected, Exposure is 3.0 in day 4 at move 0
*When No. 643 infected, Exposure is 2.0 in day 4 at move 0
*When No. 304 infected, Exposure is 2.0 in day 4 at move 1
*When No. 646 infected, Exposure is 3.0 in day 4 at move 1
*When No. 770 infected, Exposure is 5.0 in day 4 at move 3
*When No. 899 infected, Exposure is 4.0 in day 4 at move 4
*When No. 902 infected, Exposure is 4.0 in day 4 at move 4
*When No. 950 infected, Exposure is 4.0 in day 4 at move 4
*When No. 996 infected, Exposure is 3.0 in day 4 at move 4
No. 2 exposure increased to 1.0 in day 4 at 5
No. 20 exposure increased to 2.0 in day 4 at 5
No. 38 exposure increased to 2.0 in day 4 at 5
No. 63 exposure increased to 1.0 in day 4 at 5
No. 89 exposure increased to 1.0 in day 4 at 5
No. 91 exposure increased to 2.0 in day 4 at 5
No. 93 exposure increased to 1.0 in day 4 at 5
No. 102 exposure increased to 2.0 in day 4 at 5
No. 103 exposure increased to 2.0 in day 4 at 5
No. 108 exposure increased to 2.0 in day 4 at 5
No. 109 exposure increased to 4.0 in day 4 at 5
No. 125 exposure increased to 4.0 in day 4 at 5
No. 135 exposure increased to 1.0 in day 4 at 5
No. 141 exposure increased to 2.0 in day 4 at 5
No. 168 exposure increased to 2.0 in day 4 at 5
No. 170 exposure increased to 1.0 in day 4 at 5
No. 173 exposure increased to 1.0 in day 4 at 5
No. 174 exposure increased to 4.0 in day 4 at 5
No. 184 exposure increased to 1.0 in day 4 at 5
No. 215 exposure increased to 2.0 in day 4 at 5
No. 239 exposure increased to 2.0 in day 4 at 5
No. 273 exposure increased to 1.0 in day 4 at 5
No. 276 exposure increased to 1.0 in day 4 at 5
No. 287 exposure increased to 1.0 in day 4 at 5
No. 297 exposure increased to 1.0 in day 4 at 5
No. 300 exposure increased to 1.0 in day 4 at 5
No. 307 exposure increased to 3.0 in day 4 at 5
No. 322 exposure increased to 1.0 in day 4 at 5
No. 326 exposure increased to 2.0 in day 4 at 5
No. 350 exposure increased to 2.0 in day 4 at 5
No. 354 exposure increased to 2.0 in day 4 at 5
No. 368 exposure increased to 2.0 in day 4 at 5
No. 373 exposure increased to 2.0 in day 4 at 5
No. 389 exposure increased to 2.0 in day 4 at 5
No. 393 exposure increased to 1.0 in day 4 at 5
No. 441 exposure increased to 6.0 in day 4 at 5
No. 446 exposure increased to 1.0 in day 4 at 5
No. 452 exposure increased to 1.0 in day 4 at 5
No. 468 exposure increased to 4.0 in day 4 at 5
No. 483 exposure increased to 1.0 in day 4 at 5
No. 495 exposure increased to 1.0 in day 4 at 5
No. 500 exposure increased to 1.0 in day 4 at 5
No. 504 exposure increased to 3.0 in day 4 at 5
No. 510 exposure increased to 2.0 in day 4 at 5
No. 514 exposure increased to 2.0 in day 4 at 5
No. 519 exposure increased to 2.0 in day 4 at 5
No. 543 exposure increased to 2.0 in day 4 at 5
No. 576 exposure increased to 1.0 in day 4 at 5
No. 587 exposure increased to 2.0 in day 4 at 5
*When No. 602 infected, Exposure is 3.0 in day 4 at move 5
No. 633 exposure increased to 2.0 in day 4 at 5
No. 649 exposure increased to 1.0 in day 4 at 5
No. 659 exposure increased to 1.0 in day 4 at 5
No. 665 exposure increased to 2.0 in day 4 at 5
No. 676 exposure increased to 2.0 in day 4 at 5
No. 687 exposure increased to 2.0 in day 4 at 5
No. 691 exposure increased to 2.0 in day 4 at 5
No. 696 exposure increased to 1.0 in day 4 at 5
No. 705 exposure increased to 1.0 in day 4 at 5
No. 718 exposure increased to 1.0 in day 4 at 5
No. 733 exposure increased to 1.0 in day 4 at 5
No. 756 exposure increased to 1.0 in day 4 at 5
No. 772 exposure increased to 2.0 in day 4 at 5
No. 803 exposure increased to 1.0 in day 4 at 5
No. 806 exposure increased to 3.0 in day 4 at 5
No. 822 exposure increased to 1.0 in day 4 at 5
No. 842 exposure increased to 1.0 in day 4 at 5
No. 862 exposure increased to 1.0 in day 4 at 5
No. 866 exposure increased to 1.0 in day 4 at 5
No. 874 exposure increased to 2.0 in day 4 at 5
No. 883 exposure increased to 3.0 in day 4 at 5
No. 884 exposure increased to 2.0 in day 4 at 5
No. 889 exposure increased to 1.0 in day 4 at 5
No. 903 exposure increased to 2.0 in day 4 at 5
No. 921 exposure increased to 2.0 in day 4 at 5
No. 922 exposure increased to 2.0 in day 4 at 5
No. 926 exposure increased to 2.0 in day 4 at 5
No. 931 exposure increased to 2.0 in day 4 at 5
*When No. 951 infected, Exposure is 3.0 in day 4 at move 5
No. 987 exposure increased to 2.0 in day 4 at 5
  138/10000 [..............................] - ETA: 17:53:30 - reward: 700.5001*When No. 125 infected, Exposure is 4.0 in day 4 at move 0
*When No. 174 infected, Exposure is 4.0 in day 4 at move 0
*When No. 307 infected, Exposure is 3.0 in day 4 at move 0
*When No. 468 infected, Exposure is 4.0 in day 4 at move 0
*When No. 108 infected, Exposure is 2.0 in day 4 at move 1
*When No. 109 infected, Exposure is 4.0 in day 4 at move 1
*When No. 587 infected, Exposure is 2.0 in day 4 at move 1
*When No. 772 infected, Exposure is 2.0 in day 4 at move 1
*When No. 884 infected, Exposure is 2.0 in day 4 at move 1
*When No. 987 infected, Exposure is 2.0 in day 4 at move 1
*When No. 38 infected, Exposure is 2.0 in day 4 at move 2
*When No. 102 infected, Exposure is 2.0 in day 4 at move 2
*When No. 103 infected, Exposure is 2.0 in day 4 at move 2
*When No. 883 infected, Exposure is 3.0 in day 4 at move 2
*When No. 903 infected, Exposure is 2.0 in day 4 at move 2
*When No. 931 infected, Exposure is 2.0 in day 4 at move 2
*When No. 326 infected, Exposure is 2.0 in day 4 at move 3
*When No. 514 infected, Exposure is 2.0 in day 4 at move 3
*When No. 350 infected, Exposure is 2.0 in day 4 at move 4
*When No. 504 infected, Exposure is 3.0 in day 4 at move 4
*When No. 806 infected, Exposure is 3.0 in day 4 at move 4
*When No. 926 infected, Exposure is 2.0 in day 4 at move 4
No. 2 exposure increased to 2.0 in day 4 at 5
*When No. 20 infected, Exposure is 2.0 in day 4 at move 5
No. 27 exposure increased to 1.0 in day 4 at 5
No. 29 exposure increased to 1.0 in day 4 at 5
No. 40 exposure increased to 1.0 in day 4 at 5
No. 50 exposure increased to 1.0 in day 4 at 5
No. 60 exposure increased to 1.0 in day 4 at 5
No. 63 exposure increased to 2.0 in day 4 at 5
No. 89 exposure increased to 2.0 in day 4 at 5
No. 91 exposure increased to 3.0 in day 4 at 5
No. 93 exposure increased to 2.0 in day 4 at 5
No. 114 exposure increased to 1.0 in day 4 at 5
No. 118 exposure increased to 1.0 in day 4 at 5
No. 135 exposure increased to 2.0 in day 4 at 5
No. 141 exposure increased to 3.0 in day 4 at 5
No. 142 exposure increased to 2.0 in day 4 at 5
No. 168 exposure increased to 3.0 in day 4 at 5
No. 170 exposure increased to 2.0 in day 4 at 5
No. 173 exposure increased to 2.0 in day 4 at 5
No. 181 exposure increased to 1.0 in day 4 at 5
No. 184 exposure increased to 2.0 in day 4 at 5
No. 191 exposure increased to 1.0 in day 4 at 5
No. 215 exposure increased to 3.0 in day 4 at 5
No. 239 exposure increased to 3.0 in day 4 at 5
No. 273 exposure increased to 2.0 in day 4 at 5
No. 276 exposure increased to 2.0 in day 4 at 5
No. 284 exposure increased to 1.0 in day 4 at 5
No. 285 exposure increased to 1.0 in day 4 at 5
No. 287 exposure increased to 2.0 in day 4 at 5
No. 293 exposure increased to 1.0 in day 4 at 5
No. 297 exposure increased to 2.0 in day 4 at 5
No. 300 exposure increased to 2.0 in day 4 at 5
No. 322 exposure increased to 2.0 in day 4 at 5
No. 329 exposure increased to 1.0 in day 4 at 5
No. 353 exposure increased to 1.0 in day 4 at 5
No. 354 exposure increased to 3.0 in day 4 at 5
*When No. 368 infected, Exposure is 2.0 in day 4 at move 5
No. 373 exposure increased to 3.0 in day 4 at 5
No. 375 exposure increased to 1.0 in day 4 at 5
No. 389 exposure increased to 3.0 in day 4 at 5
No. 393 exposure increased to 2.0 in day 4 at 5
No. 409 exposure increased to 1.0 in day 4 at 5
No. 417 exposure increased to 1.0 in day 4 at 5
No. 433 exposure increased to 1.0 in day 4 at 5
*When No. 441 infected, Exposure is 6.0 in day 4 at move 5
No. 446 exposure increased to 2.0 in day 4 at 5
No. 448 exposure increased to 1.0 in day 4 at 5
No. 450 exposure increased to 1.0 in day 4 at 5
No. 452 exposure increased to 2.0 in day 4 at 5
No. 483 exposure increased to 2.0 in day 4 at 5
No. 495 exposure increased to 2.0 in day 4 at 5
No. 500 exposure increased to 2.0 in day 4 at 5
No. 510 exposure increased to 3.0 in day 4 at 5
No. 519 exposure increased to 3.0 in day 4 at 5
No. 543 exposure increased to 3.0 in day 4 at 5
No. 547 exposure increased to 1.0 in day 4 at 5
No. 572 exposure increased to 1.0 in day 4 at 5
No. 575 exposure increased to 1.0 in day 4 at 5
No. 576 exposure increased to 2.0 in day 4 at 5
No. 609 exposure increased to 1.0 in day 4 at 5
No. 631 exposure increased to 1.0 in day 4 at 5
No. 633 exposure increased to 3.0 in day 4 at 5
No. 649 exposure increased to 2.0 in day 4 at 5
No. 659 exposure increased to 2.0 in day 4 at 5
*When No. 665 infected, Exposure is 2.0 in day 4 at move 5
No. 676 exposure increased to 3.0 in day 4 at 5
No. 687 exposure increased to 3.0 in day 4 at 5
*When No. 691 infected, Exposure is 2.0 in day 4 at move 5
No. 696 exposure increased to 2.0 in day 4 at 5
No. 705 exposure increased to 2.0 in day 4 at 5
No. 718 exposure increased to 2.0 in day 4 at 5
No. 733 exposure increased to 2.0 in day 4 at 5
No. 743 exposure increased to 1.0 in day 4 at 5
No. 756 exposure increased to 2.0 in day 4 at 5
No. 803 exposure increased to 2.0 in day 4 at 5
No. 822 exposure increased to 2.0 in day 4 at 5
No. 835 exposure increased to 1.0 in day 4 at 5
No. 842 exposure increased to 2.0 in day 4 at 5
No. 862 exposure increased to 2.0 in day 4 at 5
No. 866 exposure increased to 2.0 in day 4 at 5
No. 874 exposure increased to 3.0 in day 4 at 5
No. 889 exposure increased to 2.0 in day 4 at 5
No. 893 exposure increased to 1.0 in day 4 at 5
No. 914 exposure increased to 1.0 in day 4 at 5
No. 921 exposure increased to 3.0 in day 4 at 5
*When No. 922 infected, Exposure is 2.0 in day 4 at move 5
No. 933 exposure increased to 1.0 in day 4 at 5
No. 946 exposure increased to 1.0 in day 4 at 5
No. 975 exposure increased to 1.0 in day 4 at 5
No. 980 exposure increased to 1.0 in day 4 at 5
No. 997 exposure increased to 1.0 in day 4 at 5
  139/10000 [..............................] - ETA: 18:02:48 - reward: 698.4278*When No. 91 infected, Exposure is 3.0 in day 4 at move 0
*When No. 93 infected, Exposure is 2.0 in day 4 at move 0
*When No. 142 infected, Exposure is 2.0 in day 4 at move 0
*When No. 239 infected, Exposure is 3.0 in day 4 at move 0
*When No. 354 infected, Exposure is 3.0 in day 4 at move 0
*When No. 373 infected, Exposure is 3.0 in day 4 at move 0
*When No. 687 infected, Exposure is 3.0 in day 4 at move 0
*When No. 756 infected, Exposure is 2.0 in day 4 at move 0
*When No. 822 infected, Exposure is 2.0 in day 4 at move 0
*When No. 874 infected, Exposure is 3.0 in day 4 at move 0
No. 2 exposure increased to 3.0 in day 4 at 1
No. 22 exposure increased to 1.0 in day 4 at 1
No. 27 exposure increased to 2.0 in day 4 at 1
No. 29 exposure increased to 2.0 in day 4 at 1
No. 40 exposure increased to 2.0 in day 4 at 1
No. 50 exposure increased to 2.0 in day 4 at 1
No. 60 exposure increased to 2.0 in day 4 at 1
No. 63 exposure increased to 3.0 in day 4 at 1
No. 89 exposure increased to 3.0 in day 4 at 1
No. 114 exposure increased to 2.0 in day 4 at 1
No. 118 exposure increased to 2.0 in day 4 at 1
No. 126 exposure increased to 1.0 in day 4 at 1
No. 135 exposure increased to 3.0 in day 4 at 1
No. 141 exposure increased to 4.0 in day 4 at 1
*When No. 168 infected, Exposure is 3.0 in day 4 at move 1
No. 170 exposure increased to 3.0 in day 4 at 1
No. 173 exposure increased to 3.0 in day 4 at 1
No. 181 exposure increased to 2.0 in day 4 at 1
No. 184 exposure increased to 3.0 in day 4 at 1
No. 191 exposure increased to 2.0 in day 4 at 1
*When No. 215 infected, Exposure is 3.0 in day 4 at move 1
No. 270 exposure increased to 2.0 in day 4 at 1
No. 273 exposure increased to 3.0 in day 4 at 1
No. 276 exposure increased to 3.0 in day 4 at 1
No. 284 exposure increased to 2.0 in day 4 at 1
No. 285 exposure increased to 2.0 in day 4 at 1
No. 287 exposure increased to 3.0 in day 4 at 1
No. 293 exposure increased to 2.0 in day 4 at 1
No. 297 exposure increased to 3.0 in day 4 at 1
No. 300 exposure increased to 3.0 in day 4 at 1
No. 311 exposure increased to 2.0 in day 4 at 1
*When No. 322 infected, Exposure is 2.0 in day 4 at move 1
No. 329 exposure increased to 2.0 in day 4 at 1
No. 353 exposure increased to 2.0 in day 4 at 1
No. 375 exposure increased to 2.0 in day 4 at 1
No. 389 exposure increased to 4.0 in day 4 at 1
No. 393 exposure increased to 3.0 in day 4 at 1
No. 409 exposure increased to 2.0 in day 4 at 1
No. 417 exposure increased to 2.0 in day 4 at 1
No. 433 exposure increased to 2.0 in day 4 at 1
No. 446 exposure increased to 3.0 in day 4 at 1
No. 448 exposure increased to 2.0 in day 4 at 1
No. 450 exposure increased to 2.0 in day 4 at 1
No. 452 exposure increased to 3.0 in day 4 at 1
No. 456 exposure increased to 2.0 in day 4 at 1
No. 483 exposure increased to 3.0 in day 4 at 1
No. 495 exposure increased to 3.0 in day 4 at 1
No. 500 exposure increased to 3.0 in day 4 at 1
No. 510 exposure increased to 4.0 in day 4 at 1
No. 511 exposure increased to 2.0 in day 4 at 1
*When No. 519 infected, Exposure is 3.0 in day 4 at move 1
No. 543 exposure increased to 4.0 in day 4 at 1
No. 547 exposure increased to 2.0 in day 4 at 1
No. 572 exposure increased to 2.0 in day 4 at 1
No. 575 exposure increased to 2.0 in day 4 at 1
No. 576 exposure increased to 3.0 in day 4 at 1
No. 609 exposure increased to 2.0 in day 4 at 1
No. 620 exposure increased to 2.0 in day 4 at 1
No. 631 exposure increased to 2.0 in day 4 at 1
No. 633 exposure increased to 4.0 in day 4 at 1
No. 649 exposure increased to 3.0 in day 4 at 1
No. 659 exposure increased to 3.0 in day 4 at 1
No. 676 exposure increased to 4.0 in day 4 at 1
No. 696 exposure increased to 3.0 in day 4 at 1
No. 705 exposure increased to 3.0 in day 4 at 1
No. 718 exposure increased to 3.0 in day 4 at 1
No. 733 exposure increased to 3.0 in day 4 at 1
No. 743 exposure increased to 2.0 in day 4 at 1
No. 801 exposure increased to 1.0 in day 4 at 1
No. 803 exposure increased to 3.0 in day 4 at 1
No. 835 exposure increased to 2.0 in day 4 at 1
No. 839 exposure increased to 1.0 in day 4 at 1
*When No. 842 infected, Exposure is 2.0 in day 4 at move 1
*When No. 862 infected, Exposure is 2.0 in day 4 at move 1
No. 866 exposure increased to 3.0 in day 4 at 1
No. 889 exposure increased to 3.0 in day 4 at 1
No. 893 exposure increased to 2.0 in day 4 at 1
No. 914 exposure increased to 2.0 in day 4 at 1
No. 921 exposure increased to 4.0 in day 4 at 1
No. 933 exposure increased to 2.0 in day 4 at 1
No. 946 exposure increased to 2.0 in day 4 at 1
No. 975 exposure increased to 2.0 in day 4 at 1
No. 980 exposure increased to 2.0 in day 4 at 1
No. 997 exposure increased to 2.0 in day 4 at 1
  140/10000 [..............................] - ETA: 18:02:26 - reward: 696.8402*When No. 2 infected, Exposure is 3.0 in day 4 at move 0
*When No. 29 infected, Exposure is 2.0 in day 4 at move 0
*When No. 184 infected, Exposure is 3.0 in day 4 at move 0
*When No. 297 infected, Exposure is 3.0 in day 4 at move 0
*When No. 329 infected, Exposure is 2.0 in day 4 at move 0
*When No. 389 infected, Exposure is 4.0 in day 4 at move 0
*When No. 433 infected, Exposure is 2.0 in day 4 at move 0
*When No. 483 infected, Exposure is 3.0 in day 4 at move 0
*When No. 511 infected, Exposure is 2.0 in day 4 at move 0
*When No. 633 infected, Exposure is 4.0 in day 4 at move 0
*When No. 835 infected, Exposure is 2.0 in day 4 at move 0
*When No. 889 infected, Exposure is 3.0 in day 4 at move 0
*When No. 141 infected, Exposure is 4.0 in day 4 at move 1
*When No. 181 infected, Exposure is 2.0 in day 4 at move 1
*When No. 300 infected, Exposure is 3.0 in day 4 at move 1
*When No. 448 infected, Exposure is 2.0 in day 4 at move 1
*When No. 452 infected, Exposure is 3.0 in day 4 at move 1
*When No. 676 infected, Exposure is 4.0 in day 4 at move 1
*When No. 743 infected, Exposure is 2.0 in day 4 at move 1
*When No. 803 infected, Exposure is 3.0 in day 4 at move 1
*When No. 866 infected, Exposure is 3.0 in day 4 at move 1
*When No. 114 infected, Exposure is 2.0 in day 4 at move 2
*When No. 135 infected, Exposure is 3.0 in day 4 at move 2
*When No. 191 infected, Exposure is 2.0 in day 4 at move 2
*When No. 284 infected, Exposure is 2.0 in day 4 at move 2
*When No. 287 infected, Exposure is 3.0 in day 4 at move 2
*When No. 576 infected, Exposure is 3.0 in day 4 at move 2
*When No. 609 infected, Exposure is 2.0 in day 4 at move 2
*When No. 914 infected, Exposure is 2.0 in day 4 at move 2
*When No. 946 infected, Exposure is 2.0 in day 4 at move 2
*When No. 170 infected, Exposure is 3.0 in day 4 at move 3
*When No. 417 infected, Exposure is 2.0 in day 4 at move 3
*When No. 495 infected, Exposure is 3.0 in day 4 at move 3
*When No. 659 infected, Exposure is 3.0 in day 4 at move 3
*When No. 921 infected, Exposure is 4.0 in day 4 at move 3
*When No. 27 infected, Exposure is 2.0 in day 4 at move 4
*When No. 89 infected, Exposure is 3.0 in day 4 at move 4
*When No. 173 infected, Exposure is 3.0 in day 4 at move 4
*When No. 276 infected, Exposure is 3.0 in day 4 at move 4
*When No. 311 infected, Exposure is 2.0 in day 4 at move 4
*When No. 375 infected, Exposure is 2.0 in day 4 at move 4
*When No. 543 infected, Exposure is 4.0 in day 4 at move 4
*When No. 733 infected, Exposure is 3.0 in day 4 at move 4
No. 0 exposure increased to 1.0 in day 4 at 5
No. 1 exposure increased to 1.0 in day 4 at 5
No. 15 exposure increased to 1.0 in day 4 at 5
No. 22 exposure increased to 2.0 in day 4 at 5
No. 24 exposure increased to 1.0 in day 4 at 5
No. 40 exposure increased to 3.0 in day 4 at 5
No. 50 exposure increased to 3.0 in day 4 at 5
No. 60 exposure increased to 3.0 in day 4 at 5
No. 63 exposure increased to 4.0 in day 4 at 5
No. 112 exposure increased to 2.0 in day 4 at 5
No. 118 exposure increased to 3.0 in day 4 at 5
No. 126 exposure increased to 2.0 in day 4 at 5
No. 130 exposure increased to 1.0 in day 4 at 5
No. 189 exposure increased to 1.0 in day 4 at 5
No. 234 exposure increased to 2.0 in day 4 at 5
No. 247 exposure increased to 2.0 in day 4 at 5
No. 263 exposure increased to 1.0 in day 4 at 5
No. 266 exposure increased to 1.0 in day 4 at 5
No. 270 exposure increased to 3.0 in day 4 at 5
No. 273 exposure increased to 4.0 in day 4 at 5
No. 285 exposure increased to 3.0 in day 4 at 5
No. 293 exposure increased to 3.0 in day 4 at 5
No. 302 exposure increased to 2.0 in day 4 at 5
No. 315 exposure increased to 2.0 in day 4 at 5
No. 342 exposure increased to 2.0 in day 4 at 5
*When No. 353 infected, Exposure is 2.0 in day 4 at move 5
No. 357 exposure increased to 1.0 in day 4 at 5
No. 379 exposure increased to 1.0 in day 4 at 5
No. 384 exposure increased to 1.0 in day 4 at 5
No. 393 exposure increased to 4.0 in day 4 at 5
No. 409 exposure increased to 3.0 in day 4 at 5
No. 446 exposure increased to 4.0 in day 4 at 5
No. 450 exposure increased to 3.0 in day 4 at 5
No. 456 exposure increased to 3.0 in day 4 at 5
No. 500 exposure increased to 4.0 in day 4 at 5
No. 510 exposure increased to 5.0 in day 4 at 5
No. 518 exposure increased to 1.0 in day 4 at 5
No. 528 exposure increased to 1.0 in day 4 at 5
No. 530 exposure increased to 1.0 in day 4 at 5
No. 535 exposure increased to 1.0 in day 4 at 5
No. 547 exposure increased to 3.0 in day 4 at 5
No. 571 exposure increased to 1.0 in day 4 at 5
No. 572 exposure increased to 3.0 in day 4 at 5
No. 575 exposure increased to 3.0 in day 4 at 5
No. 611 exposure increased to 1.0 in day 4 at 5
No. 615 exposure increased to 1.0 in day 4 at 5
No. 618 exposure increased to 1.0 in day 4 at 5
No. 620 exposure increased to 3.0 in day 4 at 5
No. 623 exposure increased to 1.0 in day 4 at 5
No. 631 exposure increased to 3.0 in day 4 at 5
No. 649 exposure increased to 4.0 in day 4 at 5
No. 682 exposure increased to 1.0 in day 4 at 5
No. 696 exposure increased to 4.0 in day 4 at 5
No. 701 exposure increased to 1.0 in day 4 at 5
No. 705 exposure increased to 4.0 in day 4 at 5
No. 718 exposure increased to 4.0 in day 4 at 5
No. 771 exposure increased to 1.0 in day 4 at 5
No. 787 exposure increased to 1.0 in day 4 at 5
No. 801 exposure increased to 2.0 in day 4 at 5
No. 839 exposure increased to 2.0 in day 4 at 5
No. 840 exposure increased to 1.0 in day 4 at 5
No. 882 exposure increased to 1.0 in day 4 at 5
No. 893 exposure increased to 3.0 in day 4 at 5
No. 900 exposure increased to 1.0 in day 4 at 5
No. 908 exposure increased to 1.0 in day 4 at 5
No. 933 exposure increased to 3.0 in day 4 at 5
No. 935 exposure increased to 1.0 in day 4 at 5
No. 961 exposure increased to 1.0 in day 4 at 5
No. 965 exposure increased to 1.0 in day 4 at 5
No. 975 exposure increased to 3.0 in day 4 at 5
No. 980 exposure increased to 3.0 in day 4 at 5
No. 997 exposure increased to 3.0 in day 4 at 5
  141/10000 [..............................] - ETA: 18:07:21 - reward: 695.0104*When No. 118 infected, Exposure is 3.0 in day 4 at move 0
*When No. 273 infected, Exposure is 4.0 in day 4 at move 0
*When No. 547 infected, Exposure is 3.0 in day 4 at move 0
*When No. 572 infected, Exposure is 3.0 in day 4 at move 0
*When No. 705 infected, Exposure is 4.0 in day 4 at move 0
*When No. 893 infected, Exposure is 3.0 in day 4 at move 0
No. 0 exposure increased to 2.0 in day 4 at 1
No. 1 exposure increased to 2.0 in day 4 at 1
No. 12 exposure increased to 2.0 in day 4 at 1
No. 15 exposure increased to 2.0 in day 4 at 1
No. 22 exposure increased to 3.0 in day 4 at 1
No. 24 exposure increased to 2.0 in day 4 at 1
No. 26 exposure increased to 2.0 in day 4 at 1
No. 28 exposure increased to 1.0 in day 4 at 1
No. 40 exposure increased to 4.0 in day 4 at 1
No. 50 exposure increased to 4.0 in day 4 at 1
No. 60 exposure increased to 4.0 in day 4 at 1
No. 63 exposure increased to 5.0 in day 4 at 1
No. 72 exposure increased to 2.0 in day 4 at 1
No. 112 exposure increased to 3.0 in day 4 at 1
No. 126 exposure increased to 3.0 in day 4 at 1
No. 130 exposure increased to 2.0 in day 4 at 1
No. 189 exposure increased to 2.0 in day 4 at 1
No. 234 exposure increased to 3.0 in day 4 at 1
*When No. 247 infected, Exposure is 2.0 in day 4 at move 1
No. 263 exposure increased to 2.0 in day 4 at 1
No. 266 exposure increased to 2.0 in day 4 at 1
No. 270 exposure increased to 4.0 in day 4 at 1
No. 285 exposure increased to 4.0 in day 4 at 1
No. 293 exposure increased to 4.0 in day 4 at 1
No. 302 exposure increased to 3.0 in day 4 at 1
No. 315 exposure increased to 3.0 in day 4 at 1
No. 342 exposure increased to 3.0 in day 4 at 1
No. 357 exposure increased to 2.0 in day 4 at 1
No. 379 exposure increased to 2.0 in day 4 at 1
No. 384 exposure increased to 2.0 in day 4 at 1
No. 393 exposure increased to 5.0 in day 4 at 1
No. 409 exposure increased to 4.0 in day 4 at 1
No. 435 exposure increased to 1.0 in day 4 at 1
No. 443 exposure increased to 1.0 in day 4 at 1
No. 446 exposure increased to 5.0 in day 4 at 1
No. 450 exposure increased to 4.0 in day 4 at 1
No. 456 exposure increased to 4.0 in day 4 at 1
No. 498 exposure increased to 1.0 in day 4 at 1
No. 500 exposure increased to 5.0 in day 4 at 1
No. 510 exposure increased to 6.0 in day 4 at 1
No. 518 exposure increased to 2.0 in day 4 at 1
No. 523 exposure increased to 2.0 in day 4 at 1
No. 528 exposure increased to 2.0 in day 4 at 1
No. 530 exposure increased to 2.0 in day 4 at 1
No. 535 exposure increased to 2.0 in day 4 at 1
No. 550 exposure increased to 1.0 in day 4 at 1
No. 571 exposure increased to 2.0 in day 4 at 1
No. 575 exposure increased to 4.0 in day 4 at 1
No. 611 exposure increased to 2.0 in day 4 at 1
No. 615 exposure increased to 2.0 in day 4 at 1
No. 618 exposure increased to 2.0 in day 4 at 1
*When No. 620 infected, Exposure is 3.0 in day 4 at move 1
No. 623 exposure increased to 2.0 in day 4 at 1
No. 631 exposure increased to 4.0 in day 4 at 1
No. 641 exposure increased to 1.0 in day 4 at 1
No. 649 exposure increased to 5.0 in day 4 at 1
No. 682 exposure increased to 2.0 in day 4 at 1
No. 696 exposure increased to 5.0 in day 4 at 1
No. 698 exposure increased to 1.0 in day 4 at 1
No. 701 exposure increased to 2.0 in day 4 at 1
*When No. 718 infected, Exposure is 4.0 in day 4 at move 1
No. 771 exposure increased to 2.0 in day 4 at 1
No. 776 exposure increased to 1.0 in day 4 at 1
No. 787 exposure increased to 2.0 in day 4 at 1
*When No. 801 infected, Exposure is 2.0 in day 4 at move 1
No. 839 exposure increased to 3.0 in day 4 at 1
No. 840 exposure increased to 2.0 in day 4 at 1
No. 882 exposure increased to 2.0 in day 4 at 1
No. 900 exposure increased to 2.0 in day 4 at 1
No. 908 exposure increased to 2.0 in day 4 at 1
No. 933 exposure increased to 4.0 in day 4 at 1
No. 935 exposure increased to 2.0 in day 4 at 1
No. 961 exposure increased to 2.0 in day 4 at 1
No. 962 exposure increased to 2.0 in day 4 at 1
No. 965 exposure increased to 2.0 in day 4 at 1
No. 975 exposure increased to 4.0 in day 4 at 1
No. 980 exposure increased to 4.0 in day 4 at 1
No. 997 exposure increased to 4.0 in day 4 at 1
  142/10000 [..............................] - ETA: 18:05:31 - reward: 693.4425*When No. 1 infected, Exposure is 2.0 in day 4 at move 0
*When No. 40 infected, Exposure is 4.0 in day 4 at move 0
*When No. 60 infected, Exposure is 4.0 in day 4 at move 0
*When No. 72 infected, Exposure is 2.0 in day 4 at move 0
*When No. 126 infected, Exposure is 3.0 in day 4 at move 0
*When No. 234 infected, Exposure is 3.0 in day 4 at move 0
*When No. 270 infected, Exposure is 4.0 in day 4 at move 0
*When No. 285 infected, Exposure is 4.0 in day 4 at move 0
*When No. 293 infected, Exposure is 4.0 in day 4 at move 0
*When No. 446 infected, Exposure is 5.0 in day 4 at move 0
*When No. 450 infected, Exposure is 4.0 in day 4 at move 0
*When No. 510 infected, Exposure is 6.0 in day 4 at move 0
*When No. 518 infected, Exposure is 2.0 in day 4 at move 0
*When No. 571 infected, Exposure is 2.0 in day 4 at move 0
*When No. 618 infected, Exposure is 2.0 in day 4 at move 0
*When No. 631 infected, Exposure is 4.0 in day 4 at move 0
*When No. 649 infected, Exposure is 5.0 in day 4 at move 0
*When No. 696 infected, Exposure is 5.0 in day 4 at move 0
*When No. 882 infected, Exposure is 2.0 in day 4 at move 0
*When No. 933 infected, Exposure is 4.0 in day 4 at move 0
*When No. 980 infected, Exposure is 4.0 in day 4 at move 0
*When No. 0 infected, Exposure is 2.0 in day 4 at move 1
*When No. 12 infected, Exposure is 2.0 in day 4 at move 1
*When No. 50 infected, Exposure is 4.0 in day 4 at move 1
*When No. 112 infected, Exposure is 3.0 in day 4 at move 1
*When No. 379 infected, Exposure is 2.0 in day 4 at move 1
*When No. 500 infected, Exposure is 5.0 in day 4 at move 1
*When No. 623 infected, Exposure is 2.0 in day 4 at move 1
*When No. 997 infected, Exposure is 4.0 in day 4 at move 1
*When No. 24 infected, Exposure is 2.0 in day 4 at move 2
*When No. 393 infected, Exposure is 5.0 in day 4 at move 2
*When No. 528 infected, Exposure is 2.0 in day 4 at move 2
*When No. 530 infected, Exposure is 2.0 in day 4 at move 2
*When No. 787 infected, Exposure is 2.0 in day 4 at move 2
*When No. 22 infected, Exposure is 3.0 in day 4 at move 3
*When No. 63 infected, Exposure is 5.0 in day 4 at move 3
*When No. 302 infected, Exposure is 3.0 in day 4 at move 3
*When No. 611 infected, Exposure is 2.0 in day 4 at move 3
*When No. 771 infected, Exposure is 2.0 in day 4 at move 3
*When No. 839 infected, Exposure is 3.0 in day 4 at move 3
*When No. 15 infected, Exposure is 2.0 in day 4 at move 4
*When No. 315 infected, Exposure is 3.0 in day 4 at move 4
*When No. 342 infected, Exposure is 3.0 in day 4 at move 4
*When No. 456 infected, Exposure is 4.0 in day 4 at move 4
*When No. 975 infected, Exposure is 4.0 in day 4 at move 4
No. 17 exposure increased to 1.0 in day 4 at 5
No. 19 exposure increased to 2.0 in day 4 at 5
No. 26 exposure increased to 3.0 in day 4 at 5
No. 28 exposure increased to 2.0 in day 4 at 5
No. 30 exposure increased to 1.0 in day 4 at 5
No. 59 exposure increased to 2.0 in day 4 at 5
No. 66 exposure increased to 1.0 in day 4 at 5
No. 79 exposure increased to 1.0 in day 4 at 5
No. 115 exposure increased to 1.0 in day 4 at 5
No. 130 exposure increased to 3.0 in day 4 at 5
No. 189 exposure increased to 3.0 in day 4 at 5
No. 205 exposure increased to 2.0 in day 4 at 5
No. 237 exposure increased to 1.0 in day 4 at 5
No. 245 exposure increased to 1.0 in day 4 at 5
No. 263 exposure increased to 3.0 in day 4 at 5
No. 266 exposure increased to 3.0 in day 4 at 5
No. 295 exposure increased to 1.0 in day 4 at 5
No. 308 exposure increased to 1.0 in day 4 at 5
No. 321 exposure increased to 1.0 in day 4 at 5
No. 324 exposure increased to 1.0 in day 4 at 5
No. 347 exposure increased to 1.0 in day 4 at 5
No. 357 exposure increased to 3.0 in day 4 at 5
No. 384 exposure increased to 3.0 in day 4 at 5
No. 392 exposure increased to 1.0 in day 4 at 5
No. 400 exposure increased to 1.0 in day 4 at 5
*When No. 409 infected, Exposure is 4.0 in day 4 at move 5
No. 425 exposure increased to 1.0 in day 4 at 5
No. 435 exposure increased to 2.0 in day 4 at 5
No. 436 exposure increased to 1.0 in day 4 at 5
No. 443 exposure increased to 2.0 in day 4 at 5
No. 444 exposure increased to 1.0 in day 4 at 5
No. 447 exposure increased to 2.0 in day 4 at 5
No. 462 exposure increased to 1.0 in day 4 at 5
No. 480 exposure increased to 1.0 in day 4 at 5
No. 488 exposure increased to 1.0 in day 4 at 5
No. 498 exposure increased to 2.0 in day 4 at 5
No. 499 exposure increased to 1.0 in day 4 at 5
No. 523 exposure increased to 3.0 in day 4 at 5
No. 535 exposure increased to 3.0 in day 4 at 5
No. 537 exposure increased to 2.0 in day 4 at 5
No. 550 exposure increased to 2.0 in day 4 at 5
No. 556 exposure increased to 1.0 in day 4 at 5
No. 561 exposure increased to 1.0 in day 4 at 5
No. 567 exposure increased to 2.0 in day 4 at 5
*When No. 575 infected, Exposure is 4.0 in day 4 at move 5
No. 606 exposure increased to 2.0 in day 4 at 5
No. 615 exposure increased to 3.0 in day 4 at 5
No. 641 exposure increased to 2.0 in day 4 at 5
No. 654 exposure increased to 1.0 in day 4 at 5
No. 682 exposure increased to 3.0 in day 4 at 5
No. 693 exposure increased to 2.0 in day 4 at 5
No. 697 exposure increased to 1.0 in day 4 at 5
No. 698 exposure increased to 2.0 in day 4 at 5
No. 701 exposure increased to 3.0 in day 4 at 5
No. 712 exposure increased to 1.0 in day 4 at 5
No. 725 exposure increased to 1.0 in day 4 at 5
No. 726 exposure increased to 1.0 in day 4 at 5
No. 728 exposure increased to 1.0 in day 4 at 5
No. 738 exposure increased to 1.0 in day 4 at 5
No. 776 exposure increased to 2.0 in day 4 at 5
No. 795 exposure increased to 1.0 in day 4 at 5
No. 840 exposure increased to 3.0 in day 4 at 5
No. 900 exposure increased to 3.0 in day 4 at 5
No. 908 exposure increased to 3.0 in day 4 at 5
No. 909 exposure increased to 1.0 in day 4 at 5
No. 919 exposure increased to 2.0 in day 4 at 5
No. 920 exposure increased to 2.0 in day 4 at 5
No. 935 exposure increased to 3.0 in day 4 at 5
No. 953 exposure increased to 1.0 in day 4 at 5
No. 961 exposure increased to 3.0 in day 4 at 5
No. 962 exposure increased to 3.0 in day 4 at 5
No. 965 exposure increased to 3.0 in day 4 at 5
  143/10000 [..............................] - ETA: 18:10:56 - reward: 691.7868*When No. 189 infected, Exposure is 3.0 in day 4 at move 0
*When No. 357 infected, Exposure is 3.0 in day 4 at move 0
*When No. 443 infected, Exposure is 2.0 in day 4 at move 0
*When No. 908 infected, Exposure is 3.0 in day 4 at move 0
*When No. 263 infected, Exposure is 3.0 in day 4 at move 1
*When No. 435 infected, Exposure is 2.0 in day 4 at move 1
*When No. 535 infected, Exposure is 3.0 in day 4 at move 1
*When No. 615 infected, Exposure is 3.0 in day 4 at move 1
*When No. 900 infected, Exposure is 3.0 in day 4 at move 1
*When No. 962 infected, Exposure is 3.0 in day 4 at move 1
*When No. 523 infected, Exposure is 3.0 in day 4 at move 2
*When No. 641 infected, Exposure is 2.0 in day 4 at move 2
*When No. 693 infected, Exposure is 2.0 in day 4 at move 2
*When No. 59 infected, Exposure is 2.0 in day 4 at move 3
*When No. 26 infected, Exposure is 3.0 in day 4 at move 4
*When No. 130 infected, Exposure is 3.0 in day 4 at move 4
*When No. 701 infected, Exposure is 3.0 in day 4 at move 4
*When No. 935 infected, Exposure is 3.0 in day 4 at move 4
*When No. 961 infected, Exposure is 3.0 in day 4 at move 4
No. 17 exposure increased to 2.0 in day 4 at 5
No. 19 exposure increased to 3.0 in day 4 at 5
No. 28 exposure increased to 3.0 in day 4 at 5
No. 30 exposure increased to 2.0 in day 4 at 5
No. 34 exposure increased to 1.0 in day 4 at 5
No. 44 exposure increased to 1.0 in day 4 at 5
No. 66 exposure increased to 2.0 in day 4 at 5
No. 79 exposure increased to 2.0 in day 4 at 5
No. 90 exposure increased to 1.0 in day 4 at 5
No. 115 exposure increased to 2.0 in day 4 at 5
No. 123 exposure increased to 1.0 in day 4 at 5
No. 149 exposure increased to 1.0 in day 4 at 5
No. 161 exposure increased to 1.0 in day 4 at 5
No. 185 exposure increased to 1.0 in day 4 at 5
No. 187 exposure increased to 2.0 in day 4 at 5
No. 205 exposure increased to 3.0 in day 4 at 5
No. 219 exposure increased to 1.0 in day 4 at 5
No. 237 exposure increased to 2.0 in day 4 at 5
No. 245 exposure increased to 2.0 in day 4 at 5
No. 266 exposure increased to 4.0 in day 4 at 5
No. 288 exposure increased to 1.0 in day 4 at 5
No. 295 exposure increased to 2.0 in day 4 at 5
No. 308 exposure increased to 2.0 in day 4 at 5
No. 321 exposure increased to 2.0 in day 4 at 5
No. 324 exposure increased to 2.0 in day 4 at 5
No. 330 exposure increased to 1.0 in day 4 at 5
No. 340 exposure increased to 1.0 in day 4 at 5
No. 347 exposure increased to 2.0 in day 4 at 5
No. 364 exposure increased to 1.0 in day 4 at 5
No. 370 exposure increased to 1.0 in day 4 at 5
No. 384 exposure increased to 4.0 in day 4 at 5
No. 392 exposure increased to 2.0 in day 4 at 5
No. 400 exposure increased to 2.0 in day 4 at 5
No. 425 exposure increased to 2.0 in day 4 at 5
No. 436 exposure increased to 2.0 in day 4 at 5
No. 444 exposure increased to 2.0 in day 4 at 5
*When No. 447 infected, Exposure is 2.0 in day 4 at move 5
No. 462 exposure increased to 2.0 in day 4 at 5
No. 465 exposure increased to 2.0 in day 4 at 5
No. 480 exposure increased to 2.0 in day 4 at 5
No. 488 exposure increased to 2.0 in day 4 at 5
No. 498 exposure increased to 3.0 in day 4 at 5
No. 499 exposure increased to 2.0 in day 4 at 5
No. 537 exposure increased to 3.0 in day 4 at 5
No. 550 exposure increased to 3.0 in day 4 at 5
No. 553 exposure increased to 1.0 in day 4 at 5
No. 556 exposure increased to 2.0 in day 4 at 5
No. 561 exposure increased to 2.0 in day 4 at 5
No. 567 exposure increased to 3.0 in day 4 at 5
No. 592 exposure increased to 1.0 in day 4 at 5
*When No. 606 infected, Exposure is 2.0 in day 4 at move 5
No. 653 exposure increased to 1.0 in day 4 at 5
No. 654 exposure increased to 2.0 in day 4 at 5
No. 670 exposure increased to 1.0 in day 4 at 5
No. 673 exposure increased to 1.0 in day 4 at 5
No. 682 exposure increased to 4.0 in day 4 at 5
No. 685 exposure increased to 1.0 in day 4 at 5
No. 689 exposure increased to 1.0 in day 4 at 5
No. 690 exposure increased to 1.0 in day 4 at 5
No. 697 exposure increased to 2.0 in day 4 at 5
No. 698 exposure increased to 3.0 in day 4 at 5
No. 712 exposure increased to 2.0 in day 4 at 5
No. 719 exposure increased to 1.0 in day 4 at 5
No. 725 exposure increased to 2.0 in day 4 at 5
No. 726 exposure increased to 2.0 in day 4 at 5
No. 728 exposure increased to 2.0 in day 4 at 5
No. 738 exposure increased to 2.0 in day 4 at 5
No. 757 exposure increased to 1.0 in day 4 at 5
No. 776 exposure increased to 3.0 in day 4 at 5
No. 795 exposure increased to 2.0 in day 4 at 5
No. 833 exposure increased to 1.0 in day 4 at 5
No. 840 exposure increased to 4.0 in day 4 at 5
No. 858 exposure increased to 1.0 in day 4 at 5
No. 904 exposure increased to 2.0 in day 4 at 5
No. 909 exposure increased to 2.0 in day 4 at 5
No. 916 exposure increased to 1.0 in day 4 at 5
No. 919 exposure increased to 3.0 in day 4 at 5
No. 920 exposure increased to 3.0 in day 4 at 5
No. 953 exposure increased to 2.0 in day 4 at 5
No. 955 exposure increased to 2.0 in day 4 at 5
No. 960 exposure increased to 2.0 in day 4 at 5
No. 965 exposure increased to 4.0 in day 4 at 5
No. 983 exposure increased to 1.0 in day 4 at 5
No. 990 exposure increased to 1.0 in day 4 at 5
  144/10000 [..............................] - ETA: 18:14:49 - reward: 689.6534*When No. 28 infected, Exposure is 3.0 in day 4 at move 0
*When No. 384 infected, Exposure is 4.0 in day 4 at move 0
*When No. 392 infected, Exposure is 2.0 in day 4 at move 0
*When No. 436 infected, Exposure is 2.0 in day 4 at move 0
*When No. 498 infected, Exposure is 3.0 in day 4 at move 0
*When No. 795 infected, Exposure is 2.0 in day 4 at move 0
*When No. 955 infected, Exposure is 2.0 in day 4 at move 0
*When No. 79 infected, Exposure is 2.0 in day 4 at move 1
*When No. 400 infected, Exposure is 2.0 in day 4 at move 1
*When No. 682 infected, Exposure is 4.0 in day 4 at move 1
*When No. 725 infected, Exposure is 2.0 in day 4 at move 1
*When No. 909 infected, Exposure is 2.0 in day 4 at move 1
*When No. 919 infected, Exposure is 3.0 in day 4 at move 1
*When No. 115 infected, Exposure is 2.0 in day 4 at move 2
*When No. 347 infected, Exposure is 2.0 in day 4 at move 2
*When No. 444 infected, Exposure is 2.0 in day 4 at move 2
*When No. 537 infected, Exposure is 3.0 in day 4 at move 2
*When No. 561 infected, Exposure is 2.0 in day 4 at move 2
*When No. 965 infected, Exposure is 4.0 in day 4 at move 2
*When No. 66 infected, Exposure is 2.0 in day 4 at move 3
*When No. 321 infected, Exposure is 2.0 in day 4 at move 3
*When No. 567 infected, Exposure is 3.0 in day 4 at move 3
*When No. 776 infected, Exposure is 3.0 in day 4 at move 3
*When No. 840 infected, Exposure is 4.0 in day 4 at move 3
*When No. 904 infected, Exposure is 2.0 in day 4 at move 3
*When No. 465 infected, Exposure is 2.0 in day 4 at move 4
*When No. 480 infected, Exposure is 2.0 in day 4 at move 4
No. 17 exposure increased to 3.0 in day 4 at 5
No. 19 exposure increased to 4.0 in day 4 at 5
No. 30 exposure increased to 3.0 in day 4 at 5
No. 34 exposure increased to 2.0 in day 4 at 5
No. 36 exposure increased to 2.0 in day 4 at 5
No. 44 exposure increased to 2.0 in day 4 at 5
No. 74 exposure increased to 2.0 in day 4 at 5
No. 78 exposure increased to 1.0 in day 4 at 5
No. 81 exposure increased to 1.0 in day 4 at 5
No. 90 exposure increased to 2.0 in day 4 at 5
No. 123 exposure increased to 2.0 in day 4 at 5
No. 143 exposure increased to 1.0 in day 4 at 5
No. 149 exposure increased to 2.0 in day 4 at 5
No. 159 exposure increased to 1.0 in day 4 at 5
No. 161 exposure increased to 2.0 in day 4 at 5
No. 162 exposure increased to 1.0 in day 4 at 5
No. 171 exposure increased to 1.0 in day 4 at 5
No. 178 exposure increased to 1.0 in day 4 at 5
No. 185 exposure increased to 2.0 in day 4 at 5
No. 187 exposure increased to 3.0 in day 4 at 5
No. 194 exposure increased to 1.0 in day 4 at 5
No. 205 exposure increased to 4.0 in day 4 at 5
No. 212 exposure increased to 1.0 in day 4 at 5
No. 219 exposure increased to 2.0 in day 4 at 5
No. 223 exposure increased to 2.0 in day 4 at 5
No. 237 exposure increased to 3.0 in day 4 at 5
*When No. 245 infected, Exposure is 2.0 in day 4 at move 5
No. 259 exposure increased to 1.0 in day 4 at 5
No. 261 exposure increased to 1.0 in day 4 at 5
No. 266 exposure increased to 5.0 in day 4 at 5
No. 274 exposure increased to 1.0 in day 4 at 5
No. 288 exposure increased to 2.0 in day 4 at 5
No. 295 exposure increased to 3.0 in day 4 at 5
No. 308 exposure increased to 3.0 in day 4 at 5
No. 324 exposure increased to 3.0 in day 4 at 5
No. 330 exposure increased to 2.0 in day 4 at 5
No. 332 exposure increased to 1.0 in day 4 at 5
No. 340 exposure increased to 2.0 in day 4 at 5
No. 341 exposure increased to 1.0 in day 4 at 5
No. 344 exposure increased to 1.0 in day 4 at 5
No. 364 exposure increased to 2.0 in day 4 at 5
No. 370 exposure increased to 2.0 in day 4 at 5
No. 403 exposure increased to 2.0 in day 4 at 5
No. 425 exposure increased to 3.0 in day 4 at 5
No. 462 exposure increased to 3.0 in day 4 at 5
No. 488 exposure increased to 3.0 in day 4 at 5
No. 499 exposure increased to 3.0 in day 4 at 5
No. 521 exposure increased to 2.0 in day 4 at 5
No. 544 exposure increased to 2.0 in day 4 at 5
No. 546 exposure increased to 2.0 in day 4 at 5
No. 550 exposure increased to 4.0 in day 4 at 5
No. 553 exposure increased to 2.0 in day 4 at 5
No. 556 exposure increased to 3.0 in day 4 at 5
No. 589 exposure increased to 1.0 in day 4 at 5
No. 592 exposure increased to 2.0 in day 4 at 5
No. 599 exposure increased to 1.0 in day 4 at 5
No. 619 exposure increased to 2.0 in day 4 at 5
No. 653 exposure increased to 2.0 in day 4 at 5
No. 654 exposure increased to 3.0 in day 4 at 5
No. 670 exposure increased to 2.0 in day 4 at 5
No. 673 exposure increased to 2.0 in day 4 at 5
No. 685 exposure increased to 2.0 in day 4 at 5
No. 688 exposure increased to 1.0 in day 4 at 5
No. 689 exposure increased to 2.0 in day 4 at 5
No. 690 exposure increased to 2.0 in day 4 at 5
No. 697 exposure increased to 3.0 in day 4 at 5
No. 698 exposure increased to 4.0 in day 4 at 5
*When No. 712 infected, Exposure is 2.0 in day 4 at move 5
No. 719 exposure increased to 2.0 in day 4 at 5
No. 726 exposure increased to 3.0 in day 4 at 5
No. 728 exposure increased to 3.0 in day 4 at 5
No. 738 exposure increased to 3.0 in day 4 at 5
No. 751 exposure increased to 1.0 in day 4 at 5
No. 754 exposure increased to 1.0 in day 4 at 5
No. 757 exposure increased to 2.0 in day 4 at 5
No. 777 exposure increased to 1.0 in day 4 at 5
No. 798 exposure increased to 1.0 in day 4 at 5
No. 830 exposure increased to 1.0 in day 4 at 5
No. 833 exposure increased to 2.0 in day 4 at 5
No. 845 exposure increased to 1.0 in day 4 at 5
No. 857 exposure increased to 1.0 in day 4 at 5
No. 858 exposure increased to 2.0 in day 4 at 5
No. 871 exposure increased to 1.0 in day 4 at 5
No. 906 exposure increased to 1.0 in day 4 at 5
No. 916 exposure increased to 2.0 in day 4 at 5
No. 920 exposure increased to 4.0 in day 4 at 5
No. 953 exposure increased to 3.0 in day 4 at 5
No. 960 exposure increased to 3.0 in day 4 at 5
No. 972 exposure increased to 1.0 in day 4 at 5
No. 983 exposure increased to 2.0 in day 4 at 5
No. 990 exposure increased to 2.0 in day 4 at 5
No. 992 exposure increased to 2.0 in day 4 at 5
  145/10000 [..............................] - ETA: 18:14:17 - reward: 687.6646*When No. 17 infected, Exposure is 3.0 in day 4 at move 0
*When No. 30 infected, Exposure is 3.0 in day 4 at move 0
*When No. 187 infected, Exposure is 3.0 in day 4 at move 0
*When No. 550 infected, Exposure is 4.0 in day 4 at move 0
*When No. 619 infected, Exposure is 2.0 in day 4 at move 0
*When No. 719 infected, Exposure is 2.0 in day 4 at move 0
*When No. 757 infected, Exposure is 2.0 in day 4 at move 0
*When No. 19 infected, Exposure is 4.0 in day 4 at move 1
No. 34 exposure increased to 3.0 in day 4 at 1
No. 36 exposure increased to 3.0 in day 4 at 1
No. 44 exposure increased to 3.0 in day 4 at 1
No. 74 exposure increased to 3.0 in day 4 at 1
No. 76 exposure increased to 1.0 in day 4 at 1
No. 78 exposure increased to 2.0 in day 4 at 1
No. 81 exposure increased to 2.0 in day 4 at 1
No. 90 exposure increased to 3.0 in day 4 at 1
No. 123 exposure increased to 3.0 in day 4 at 1
No. 129 exposure increased to 2.0 in day 4 at 1
No. 143 exposure increased to 2.0 in day 4 at 1
No. 149 exposure increased to 3.0 in day 4 at 1
No. 159 exposure increased to 2.0 in day 4 at 1
No. 161 exposure increased to 3.0 in day 4 at 1
No. 162 exposure increased to 2.0 in day 4 at 1
No. 171 exposure increased to 2.0 in day 4 at 1
No. 178 exposure increased to 2.0 in day 4 at 1
No. 185 exposure increased to 3.0 in day 4 at 1
No. 194 exposure increased to 2.0 in day 4 at 1
*When No. 205 infected, Exposure is 4.0 in day 4 at move 1
No. 212 exposure increased to 2.0 in day 4 at 1
No. 219 exposure increased to 3.0 in day 4 at 1
No. 223 exposure increased to 3.0 in day 4 at 1
No. 235 exposure increased to 2.0 in day 4 at 1
No. 237 exposure increased to 4.0 in day 4 at 1
No. 259 exposure increased to 2.0 in day 4 at 1
No. 261 exposure increased to 2.0 in day 4 at 1
No. 266 exposure increased to 6.0 in day 4 at 1
No. 274 exposure increased to 2.0 in day 4 at 1
No. 288 exposure increased to 3.0 in day 4 at 1
*When No. 295 infected, Exposure is 3.0 in day 4 at move 1
No. 308 exposure increased to 4.0 in day 4 at 1
No. 320 exposure increased to 2.0 in day 4 at 1
No. 324 exposure increased to 4.0 in day 4 at 1
No. 330 exposure increased to 3.0 in day 4 at 1
No. 332 exposure increased to 2.0 in day 4 at 1
No. 335 exposure increased to 2.0 in day 4 at 1
No. 340 exposure increased to 3.0 in day 4 at 1
No. 341 exposure increased to 2.0 in day 4 at 1
No. 344 exposure increased to 2.0 in day 4 at 1
No. 364 exposure increased to 3.0 in day 4 at 1
No. 370 exposure increased to 3.0 in day 4 at 1
No. 390 exposure increased to 1.0 in day 4 at 1
No. 403 exposure increased to 3.0 in day 4 at 1
No. 425 exposure increased to 4.0 in day 4 at 1
No. 442 exposure increased to 1.0 in day 4 at 1
No. 462 exposure increased to 4.0 in day 4 at 1
No. 488 exposure increased to 4.0 in day 4 at 1
No. 499 exposure increased to 4.0 in day 4 at 1
No. 521 exposure increased to 3.0 in day 4 at 1
No. 544 exposure increased to 3.0 in day 4 at 1
No. 546 exposure increased to 3.0 in day 4 at 1
No. 553 exposure increased to 3.0 in day 4 at 1
No. 556 exposure increased to 4.0 in day 4 at 1
No. 589 exposure increased to 2.0 in day 4 at 1
No. 592 exposure increased to 3.0 in day 4 at 1
No. 599 exposure increased to 2.0 in day 4 at 1
No. 613 exposure increased to 2.0 in day 4 at 1
No. 653 exposure increased to 3.0 in day 4 at 1
*When No. 654 infected, Exposure is 3.0 in day 4 at move 1
No. 663 exposure increased to 1.0 in day 4 at 1
No. 669 exposure increased to 2.0 in day 4 at 1
No. 670 exposure increased to 3.0 in day 4 at 1
No. 673 exposure increased to 3.0 in day 4 at 1
No. 685 exposure increased to 3.0 in day 4 at 1
No. 688 exposure increased to 2.0 in day 4 at 1
No. 689 exposure increased to 3.0 in day 4 at 1
No. 690 exposure increased to 3.0 in day 4 at 1
No. 697 exposure increased to 4.0 in day 4 at 1
No. 698 exposure increased to 5.0 in day 4 at 1
No. 710 exposure increased to 1.0 in day 4 at 1
No. 726 exposure increased to 4.0 in day 4 at 1
*When No. 728 infected, Exposure is 3.0 in day 4 at move 1
No. 738 exposure increased to 4.0 in day 4 at 1
No. 751 exposure increased to 2.0 in day 4 at 1
No. 754 exposure increased to 2.0 in day 4 at 1
No. 777 exposure increased to 2.0 in day 4 at 1
No. 798 exposure increased to 2.0 in day 4 at 1
No. 830 exposure increased to 2.0 in day 4 at 1
No. 833 exposure increased to 3.0 in day 4 at 1
No. 845 exposure increased to 2.0 in day 4 at 1
No. 857 exposure increased to 2.0 in day 4 at 1
No. 858 exposure increased to 3.0 in day 4 at 1
No. 871 exposure increased to 2.0 in day 4 at 1
No. 906 exposure increased to 2.0 in day 4 at 1
No. 916 exposure increased to 3.0 in day 4 at 1
No. 920 exposure increased to 5.0 in day 4 at 1
No. 953 exposure increased to 4.0 in day 4 at 1
No. 960 exposure increased to 4.0 in day 4 at 1
No. 972 exposure increased to 2.0 in day 4 at 1
No. 983 exposure increased to 3.0 in day 4 at 1
*When No. 990 infected, Exposure is 2.0 in day 4 at move 1
No. 992 exposure increased to 3.0 in day 4 at 1
  146/10000 [..............................] - ETA: 18:10:47 - reward: 686.0805*When No. 36 infected, Exposure is 3.0 in day 4 at move 0
*When No. 129 infected, Exposure is 2.0 in day 4 at move 0
*When No. 143 infected, Exposure is 2.0 in day 4 at move 0
*When No. 178 infected, Exposure is 2.0 in day 4 at move 0
*When No. 194 infected, Exposure is 2.0 in day 4 at move 0
*When No. 212 infected, Exposure is 2.0 in day 4 at move 0
*When No. 266 infected, Exposure is 6.0 in day 4 at move 0
*When No. 332 infected, Exposure is 2.0 in day 4 at move 0
*When No. 344 infected, Exposure is 2.0 in day 4 at move 0
*When No. 462 infected, Exposure is 4.0 in day 4 at move 0
*When No. 499 infected, Exposure is 4.0 in day 4 at move 0
*When No. 653 infected, Exposure is 3.0 in day 4 at move 0
*When No. 690 infected, Exposure is 3.0 in day 4 at move 0
*When No. 697 infected, Exposure is 4.0 in day 4 at move 0
*When No. 726 infected, Exposure is 4.0 in day 4 at move 0
*When No. 830 infected, Exposure is 2.0 in day 4 at move 0
*When No. 858 infected, Exposure is 3.0 in day 4 at move 0
*When No. 916 infected, Exposure is 3.0 in day 4 at move 0
*When No. 992 infected, Exposure is 3.0 in day 4 at move 0
No. 34 exposure increased to 4.0 in day 4 at 1
No. 44 exposure increased to 4.0 in day 4 at 1
No. 74 exposure increased to 4.0 in day 4 at 1
No. 76 exposure increased to 2.0 in day 4 at 1
No. 78 exposure increased to 3.0 in day 4 at 1
*When No. 81 infected, Exposure is 2.0 in day 4 at move 1
*When No. 90 infected, Exposure is 3.0 in day 4 at move 1
No. 95 exposure increased to 1.0 in day 4 at 1
No. 119 exposure increased to 1.0 in day 4 at 1
No. 123 exposure increased to 4.0 in day 4 at 1
No. 149 exposure increased to 4.0 in day 4 at 1
No. 159 exposure increased to 3.0 in day 4 at 1
No. 161 exposure increased to 4.0 in day 4 at 1
No. 162 exposure increased to 3.0 in day 4 at 1
No. 171 exposure increased to 3.0 in day 4 at 1
No. 185 exposure increased to 4.0 in day 4 at 1
No. 219 exposure increased to 4.0 in day 4 at 1
*When No. 223 infected, Exposure is 3.0 in day 4 at move 1
No. 235 exposure increased to 3.0 in day 4 at 1
No. 237 exposure increased to 5.0 in day 4 at 1
No. 259 exposure increased to 3.0 in day 4 at 1
No. 261 exposure increased to 3.0 in day 4 at 1
No. 274 exposure increased to 3.0 in day 4 at 1
No. 288 exposure increased to 4.0 in day 4 at 1
No. 308 exposure increased to 5.0 in day 4 at 1
No. 320 exposure increased to 3.0 in day 4 at 1
No. 324 exposure increased to 5.0 in day 4 at 1
*When No. 330 infected, Exposure is 3.0 in day 4 at move 1
No. 335 exposure increased to 3.0 in day 4 at 1
No. 340 exposure increased to 4.0 in day 4 at 1
No. 341 exposure increased to 3.0 in day 4 at 1
No. 364 exposure increased to 4.0 in day 4 at 1
*When No. 370 infected, Exposure is 3.0 in day 4 at move 1
No. 390 exposure increased to 2.0 in day 4 at 1
No. 403 exposure increased to 4.0 in day 4 at 1
No. 425 exposure increased to 5.0 in day 4 at 1
No. 442 exposure increased to 2.0 in day 4 at 1
No. 488 exposure increased to 5.0 in day 4 at 1
No. 496 exposure increased to 1.0 in day 4 at 1
No. 521 exposure increased to 4.0 in day 4 at 1
No. 544 exposure increased to 4.0 in day 4 at 1
*When No. 546 infected, Exposure is 3.0 in day 4 at move 1
No. 553 exposure increased to 4.0 in day 4 at 1
No. 556 exposure increased to 5.0 in day 4 at 1
No. 589 exposure increased to 3.0 in day 4 at 1
No. 592 exposure increased to 4.0 in day 4 at 1
No. 599 exposure increased to 3.0 in day 4 at 1
No. 613 exposure increased to 3.0 in day 4 at 1
No. 625 exposure increased to 2.0 in day 4 at 1
No. 663 exposure increased to 2.0 in day 4 at 1
No. 669 exposure increased to 3.0 in day 4 at 1
No. 670 exposure increased to 4.0 in day 4 at 1
No. 673 exposure increased to 4.0 in day 4 at 1
*When No. 685 infected, Exposure is 3.0 in day 4 at move 1
No. 688 exposure increased to 3.0 in day 4 at 1
*When No. 689 infected, Exposure is 3.0 in day 4 at move 1
No. 694 exposure increased to 2.0 in day 4 at 1
No. 698 exposure increased to 6.0 in day 4 at 1
No. 710 exposure increased to 2.0 in day 4 at 1
No. 738 exposure increased to 5.0 in day 4 at 1
No. 751 exposure increased to 3.0 in day 4 at 1
No. 752 exposure increased to 2.0 in day 4 at 1
No. 754 exposure increased to 3.0 in day 4 at 1
No. 759 exposure increased to 1.0 in day 4 at 1
*When No. 777 infected, Exposure is 2.0 in day 4 at move 1
No. 798 exposure increased to 3.0 in day 4 at 1
No. 833 exposure increased to 4.0 in day 4 at 1
No. 845 exposure increased to 3.0 in day 4 at 1
No. 857 exposure increased to 3.0 in day 4 at 1
*When No. 871 infected, Exposure is 2.0 in day 4 at move 1
No. 906 exposure increased to 3.0 in day 4 at 1
No. 920 exposure increased to 6.0 in day 4 at 1
No. 953 exposure increased to 5.0 in day 4 at 1
*When No. 960 infected, Exposure is 4.0 in day 4 at move 1
No. 972 exposure increased to 3.0 in day 4 at 1
No. 983 exposure increased to 4.0 in day 4 at 1
  147/10000 [..............................] - ETA: 18:08:19 - reward: 683.9646*When No. 34 infected, Exposure is 4.0 in day 4 at move 0
*When No. 149 infected, Exposure is 4.0 in day 4 at move 0
*When No. 171 infected, Exposure is 3.0 in day 4 at move 0
*When No. 274 infected, Exposure is 3.0 in day 4 at move 0
*When No. 324 infected, Exposure is 5.0 in day 4 at move 0
*When No. 335 infected, Exposure is 3.0 in day 4 at move 0
*When No. 553 infected, Exposure is 4.0 in day 4 at move 0
*When No. 589 infected, Exposure is 3.0 in day 4 at move 0
*When No. 673 infected, Exposure is 4.0 in day 4 at move 0
*When No. 698 infected, Exposure is 6.0 in day 4 at move 0
*When No. 738 infected, Exposure is 5.0 in day 4 at move 0
*When No. 754 infected, Exposure is 3.0 in day 4 at move 0
*When No. 833 infected, Exposure is 4.0 in day 4 at move 0
*When No. 920 infected, Exposure is 6.0 in day 4 at move 0
*When No. 972 infected, Exposure is 3.0 in day 4 at move 0
No. 44 exposure increased to 5.0 in day 4 at 1
No. 74 exposure increased to 5.0 in day 4 at 1
No. 76 exposure increased to 3.0 in day 4 at 1
No. 78 exposure increased to 4.0 in day 4 at 1
No. 95 exposure increased to 2.0 in day 4 at 1
No. 119 exposure increased to 2.0 in day 4 at 1
No. 123 exposure increased to 5.0 in day 4 at 1
No. 159 exposure increased to 4.0 in day 4 at 1
No. 161 exposure increased to 5.0 in day 4 at 1
No. 162 exposure increased to 4.0 in day 4 at 1
*When No. 185 infected, Exposure is 4.0 in day 4 at move 1
No. 219 exposure increased to 5.0 in day 4 at 1
No. 235 exposure increased to 4.0 in day 4 at 1
No. 237 exposure increased to 6.0 in day 4 at 1
No. 241 exposure increased to 2.0 in day 4 at 1
No. 250 exposure increased to 2.0 in day 4 at 1
No. 259 exposure increased to 4.0 in day 4 at 1
No. 261 exposure increased to 4.0 in day 4 at 1
No. 288 exposure increased to 5.0 in day 4 at 1
*When No. 308 infected, Exposure is 5.0 in day 4 at move 1
No. 320 exposure increased to 4.0 in day 4 at 1
No. 340 exposure increased to 5.0 in day 4 at 1
No. 341 exposure increased to 4.0 in day 4 at 1
No. 364 exposure increased to 5.0 in day 4 at 1
No. 390 exposure increased to 3.0 in day 4 at 1
No. 399 exposure increased to 1.0 in day 4 at 1
*When No. 403 infected, Exposure is 4.0 in day 4 at move 1
*When No. 425 infected, Exposure is 5.0 in day 4 at move 1
No. 442 exposure increased to 3.0 in day 4 at 1
No. 488 exposure increased to 6.0 in day 4 at 1
No. 496 exposure increased to 2.0 in day 4 at 1
No. 517 exposure increased to 2.0 in day 4 at 1
*When No. 521 infected, Exposure is 4.0 in day 4 at move 1
No. 525 exposure increased to 1.0 in day 4 at 1
No. 544 exposure increased to 5.0 in day 4 at 1
*When No. 556 infected, Exposure is 5.0 in day 4 at move 1
No. 568 exposure increased to 1.0 in day 4 at 1
No. 574 exposure increased to 1.0 in day 4 at 1
No. 592 exposure increased to 5.0 in day 4 at 1
No. 599 exposure increased to 4.0 in day 4 at 1
No. 613 exposure increased to 4.0 in day 4 at 1
No. 616 exposure increased to 2.0 in day 4 at 1
No. 625 exposure increased to 3.0 in day 4 at 1
No. 632 exposure increased to 2.0 in day 4 at 1
*When No. 663 infected, Exposure is 2.0 in day 4 at move 1
No. 669 exposure increased to 4.0 in day 4 at 1
*When No. 670 infected, Exposure is 4.0 in day 4 at move 1
No. 688 exposure increased to 4.0 in day 4 at 1
No. 694 exposure increased to 3.0 in day 4 at 1
No. 710 exposure increased to 3.0 in day 4 at 1
No. 751 exposure increased to 4.0 in day 4 at 1
No. 752 exposure increased to 3.0 in day 4 at 1
No. 759 exposure increased to 2.0 in day 4 at 1
No. 786 exposure increased to 2.0 in day 4 at 1
No. 798 exposure increased to 4.0 in day 4 at 1
*When No. 845 infected, Exposure is 3.0 in day 4 at move 1
No. 851 exposure increased to 2.0 in day 4 at 1
No. 857 exposure increased to 4.0 in day 4 at 1
No. 881 exposure increased to 1.0 in day 4 at 1
No. 906 exposure increased to 4.0 in day 4 at 1
No. 932 exposure increased to 1.0 in day 4 at 1
No. 953 exposure increased to 6.0 in day 4 at 1
*When No. 983 infected, Exposure is 4.0 in day 4 at move 1
  148/10000 [..............................] - ETA: 18:04:05 - reward: 682.2084*When No. 74 infected, Exposure is 5.0 in day 4 at move 0
*When No. 78 infected, Exposure is 4.0 in day 4 at move 0
*When No. 123 infected, Exposure is 5.0 in day 4 at move 0
*When No. 159 infected, Exposure is 4.0 in day 4 at move 0
*When No. 162 infected, Exposure is 4.0 in day 4 at move 0
*When No. 219 infected, Exposure is 5.0 in day 4 at move 0
*When No. 259 infected, Exposure is 4.0 in day 4 at move 0
*When No. 261 infected, Exposure is 4.0 in day 4 at move 0
*When No. 288 infected, Exposure is 5.0 in day 4 at move 0
*When No. 341 infected, Exposure is 4.0 in day 4 at move 0
*When No. 364 infected, Exposure is 5.0 in day 4 at move 0
*When No. 688 infected, Exposure is 4.0 in day 4 at move 0
*When No. 710 infected, Exposure is 3.0 in day 4 at move 0
*When No. 751 infected, Exposure is 4.0 in day 4 at move 0
*When No. 857 infected, Exposure is 4.0 in day 4 at move 0
*When No. 953 infected, Exposure is 6.0 in day 4 at move 0
*When No. 390 infected, Exposure is 3.0 in day 4 at move 1
*When No. 488 infected, Exposure is 6.0 in day 4 at move 1
*When No. 599 infected, Exposure is 4.0 in day 4 at move 1
*When No. 625 infected, Exposure is 3.0 in day 4 at move 1
*When No. 798 infected, Exposure is 4.0 in day 4 at move 1
*When No. 76 infected, Exposure is 3.0 in day 4 at move 2
*When No. 95 infected, Exposure is 2.0 in day 4 at move 2
*When No. 119 infected, Exposure is 2.0 in day 4 at move 2
*When No. 161 infected, Exposure is 5.0 in day 4 at move 2
*When No. 237 infected, Exposure is 6.0 in day 4 at move 2
*When No. 496 infected, Exposure is 2.0 in day 4 at move 2
*When No. 544 infected, Exposure is 5.0 in day 4 at move 2
*When No. 669 infected, Exposure is 4.0 in day 4 at move 2
*When No. 694 infected, Exposure is 3.0 in day 4 at move 2
*When No. 250 infected, Exposure is 2.0 in day 4 at move 3
*When No. 320 infected, Exposure is 4.0 in day 4 at move 3
*When No. 340 infected, Exposure is 5.0 in day 4 at move 3
*When No. 235 infected, Exposure is 4.0 in day 4 at move 4
*When No. 906 infected, Exposure is 4.0 in day 4 at move 4
No. 44 exposure increased to 6.0 in day 4 at 5
No. 49 exposure increased to 1.0 in day 4 at 5
No. 80 exposure increased to 2.0 in day 4 at 5
No. 86 exposure increased to 1.0 in day 4 at 5
No. 111 exposure increased to 1.0 in day 4 at 5
No. 121 exposure increased to 1.0 in day 4 at 5
No. 138 exposure increased to 1.0 in day 4 at 5
No. 153 exposure increased to 1.0 in day 4 at 5
No. 177 exposure increased to 2.0 in day 4 at 5
No. 198 exposure increased to 1.0 in day 4 at 5
No. 241 exposure increased to 3.0 in day 4 at 5
No. 275 exposure increased to 1.0 in day 4 at 5
No. 286 exposure increased to 1.0 in day 4 at 5
No. 380 exposure increased to 2.0 in day 4 at 5
No. 399 exposure increased to 2.0 in day 4 at 5
No. 410 exposure increased to 2.0 in day 4 at 5
*When No. 442 infected, Exposure is 3.0 in day 4 at move 5
No. 460 exposure increased to 1.0 in day 4 at 5
No. 479 exposure increased to 1.0 in day 4 at 5
No. 517 exposure increased to 3.0 in day 4 at 5
No. 525 exposure increased to 2.0 in day 4 at 5
No. 538 exposure increased to 1.0 in day 4 at 5
No. 545 exposure increased to 1.0 in day 4 at 5
No. 568 exposure increased to 2.0 in day 4 at 5
No. 574 exposure increased to 2.0 in day 4 at 5
No. 592 exposure increased to 6.0 in day 4 at 5
No. 613 exposure increased to 5.0 in day 4 at 5
No. 616 exposure increased to 3.0 in day 4 at 5
No. 617 exposure increased to 1.0 in day 4 at 5
No. 632 exposure increased to 3.0 in day 4 at 5
No. 636 exposure increased to 1.0 in day 4 at 5
No. 711 exposure increased to 1.0 in day 4 at 5
No. 729 exposure increased to 1.0 in day 4 at 5
No. 752 exposure increased to 4.0 in day 4 at 5
No. 758 exposure increased to 1.0 in day 4 at 5
No. 759 exposure increased to 3.0 in day 4 at 5
No. 786 exposure increased to 3.0 in day 4 at 5
*When No. 851 infected, Exposure is 2.0 in day 4 at move 5
No. 881 exposure increased to 2.0 in day 4 at 5
No. 932 exposure increased to 2.0 in day 4 at 5
No. 939 exposure increased to 1.0 in day 4 at 5
  149/10000 [..............................] - ETA: 18:04:07 - reward: 680.3168*When No. 44 infected, Exposure is 6.0 in day 4 at move 0
*When No. 525 infected, Exposure is 2.0 in day 4 at move 0
*When No. 592 infected, Exposure is 6.0 in day 4 at move 0
*When No. 613 infected, Exposure is 5.0 in day 4 at move 0
*When No. 786 infected, Exposure is 3.0 in day 4 at move 0
*When No. 932 infected, Exposure is 2.0 in day 4 at move 0
No. 21 exposure increased to 2.0 in day 4 at 1
No. 35 exposure increased to 2.0 in day 4 at 1
No. 49 exposure increased to 2.0 in day 4 at 1
No. 58 exposure increased to 1.0 in day 4 at 1
No. 80 exposure increased to 3.0 in day 4 at 1
No. 86 exposure increased to 2.0 in day 4 at 1
No. 111 exposure increased to 2.0 in day 4 at 1
No. 121 exposure increased to 2.0 in day 4 at 1
No. 138 exposure increased to 2.0 in day 4 at 1
No. 153 exposure increased to 2.0 in day 4 at 1
*When No. 177 infected, Exposure is 2.0 in day 4 at move 1
No. 198 exposure increased to 2.0 in day 4 at 1
No. 204 exposure increased to 1.0 in day 4 at 1
No. 241 exposure increased to 4.0 in day 4 at 1
No. 275 exposure increased to 2.0 in day 4 at 1
No. 286 exposure increased to 2.0 in day 4 at 1
No. 298 exposure increased to 2.0 in day 4 at 1
No. 369 exposure increased to 1.0 in day 4 at 1
No. 380 exposure increased to 3.0 in day 4 at 1
No. 399 exposure increased to 3.0 in day 4 at 1
No. 410 exposure increased to 3.0 in day 4 at 1
No. 460 exposure increased to 2.0 in day 4 at 1
No. 479 exposure increased to 2.0 in day 4 at 1
No. 517 exposure increased to 4.0 in day 4 at 1
No. 538 exposure increased to 2.0 in day 4 at 1
No. 545 exposure increased to 2.0 in day 4 at 1
No. 568 exposure increased to 3.0 in day 4 at 1
No. 574 exposure increased to 3.0 in day 4 at 1
*When No. 616 infected, Exposure is 3.0 in day 4 at move 1
No. 617 exposure increased to 2.0 in day 4 at 1
No. 632 exposure increased to 4.0 in day 4 at 1
No. 636 exposure increased to 2.0 in day 4 at 1
No. 711 exposure increased to 2.0 in day 4 at 1
No. 729 exposure increased to 2.0 in day 4 at 1
No. 752 exposure increased to 5.0 in day 4 at 1
No. 758 exposure increased to 2.0 in day 4 at 1
No. 759 exposure increased to 4.0 in day 4 at 1
No. 829 exposure increased to 2.0 in day 4 at 1
No. 881 exposure increased to 3.0 in day 4 at 1
No. 939 exposure increased to 2.0 in day 4 at 1
  150/10000 [..............................] - ETA: 18:00:51 - reward: 678.7707*When No. 80 infected, Exposure is 3.0 in day 4 at move 0
*When No. 298 infected, Exposure is 2.0 in day 4 at move 0
*When No. 399 infected, Exposure is 3.0 in day 4 at move 0
*When No. 460 infected, Exposure is 2.0 in day 4 at move 0
*When No. 632 infected, Exposure is 4.0 in day 4 at move 0
*When No. 752 infected, Exposure is 5.0 in day 4 at move 0
*When No. 35 infected, Exposure is 2.0 in day 4 at move 1
*When No. 153 infected, Exposure is 2.0 in day 4 at move 1
*When No. 410 infected, Exposure is 3.0 in day 4 at move 1
*When No. 574 infected, Exposure is 3.0 in day 4 at move 1
*When No. 138 infected, Exposure is 2.0 in day 4 at move 2
*When No. 286 infected, Exposure is 2.0 in day 4 at move 2
*When No. 49 infected, Exposure is 2.0 in day 4 at move 3
*When No. 380 infected, Exposure is 3.0 in day 4 at move 3
*When No. 517 infected, Exposure is 4.0 in day 4 at move 3
*When No. 829 infected, Exposure is 2.0 in day 4 at move 3
*When No. 241 infected, Exposure is 4.0 in day 4 at move 4
*When No. 759 infected, Exposure is 4.0 in day 4 at move 4
No. 16 exposure increased to 2.0 in day 4 at 5
No. 21 exposure increased to 3.0 in day 4 at 5
No. 58 exposure increased to 2.0 in day 4 at 5
No. 61 exposure increased to 1.0 in day 4 at 5
*When No. 86 infected, Exposure is 2.0 in day 4 at move 5
No. 111 exposure increased to 3.0 in day 4 at 5
No. 113 exposure increased to 1.0 in day 4 at 5
No. 121 exposure increased to 3.0 in day 4 at 5
No. 190 exposure increased to 1.0 in day 4 at 5
No. 198 exposure increased to 3.0 in day 4 at 5
No. 204 exposure increased to 2.0 in day 4 at 5
No. 230 exposure increased to 1.0 in day 4 at 5
No. 246 exposure increased to 1.0 in day 4 at 5
No. 275 exposure increased to 3.0 in day 4 at 5
No. 327 exposure increased to 1.0 in day 4 at 5
No. 369 exposure increased to 2.0 in day 4 at 5
No. 431 exposure increased to 1.0 in day 4 at 5
No. 479 exposure increased to 3.0 in day 4 at 5
No. 482 exposure increased to 1.0 in day 4 at 5
No. 484 exposure increased to 1.0 in day 4 at 5
No. 538 exposure increased to 3.0 in day 4 at 5
No. 545 exposure increased to 3.0 in day 4 at 5
No. 568 exposure increased to 4.0 in day 4 at 5
No. 617 exposure increased to 3.0 in day 4 at 5
No. 636 exposure increased to 3.0 in day 4 at 5
No. 711 exposure increased to 3.0 in day 4 at 5
No. 729 exposure increased to 3.0 in day 4 at 5
No. 758 exposure increased to 3.0 in day 4 at 5
No. 799 exposure increased to 2.0 in day 4 at 5
No. 881 exposure increased to 4.0 in day 4 at 5
No. 939 exposure increased to 3.0 in day 4 at 5
No. 958 exposure increased to 1.0 in day 4 at 5
No. 976 exposure increased to 1.0 in day 4 at 5
No. 978 exposure increased to 1.0 in day 4 at 5
  151/10000 [..............................] - ETA: 18:00:00 - reward: 677.2000*When No. 198 infected, Exposure is 3.0 in day 4 at move 0
*When No. 275 infected, Exposure is 3.0 in day 4 at move 0
*When No. 538 infected, Exposure is 3.0 in day 4 at move 0
*When No. 568 infected, Exposure is 4.0 in day 4 at move 1
*When No. 617 infected, Exposure is 3.0 in day 4 at move 1
*When No. 729 infected, Exposure is 3.0 in day 4 at move 1
*When No. 479 infected, Exposure is 3.0 in day 4 at move 2
*When No. 636 infected, Exposure is 3.0 in day 4 at move 2
*When No. 711 infected, Exposure is 3.0 in day 4 at move 2
*When No. 16 infected, Exposure is 2.0 in day 4 at move 3
*When No. 799 infected, Exposure is 2.0 in day 4 at move 3
*When No. 881 infected, Exposure is 4.0 in day 4 at move 3
*When No. 121 infected, Exposure is 3.0 in day 4 at move 4
*When No. 545 infected, Exposure is 3.0 in day 4 at move 4
*When No. 939 infected, Exposure is 3.0 in day 4 at move 4
No. 21 exposure increased to 4.0 in day 4 at 5
No. 58 exposure increased to 3.0 in day 4 at 5
No. 61 exposure increased to 2.0 in day 4 at 5
No. 85 exposure increased to 1.0 in day 4 at 5
*When No. 111 infected, Exposure is 3.0 in day 4 at move 5
No. 113 exposure increased to 2.0 in day 4 at 5
No. 190 exposure increased to 2.0 in day 4 at 5
No. 204 exposure increased to 3.0 in day 4 at 5
No. 230 exposure increased to 2.0 in day 4 at 5
No. 243 exposure increased to 1.0 in day 4 at 5
No. 246 exposure increased to 2.0 in day 4 at 5
No. 327 exposure increased to 2.0 in day 4 at 5
*When No. 369 infected, Exposure is 2.0 in day 4 at move 5
No. 431 exposure increased to 2.0 in day 4 at 5
No. 475 exposure increased to 2.0 in day 4 at 5
No. 482 exposure increased to 2.0 in day 4 at 5
No. 484 exposure increased to 2.0 in day 4 at 5
No. 569 exposure increased to 1.0 in day 4 at 5
No. 686 exposure increased to 1.0 in day 4 at 5
No. 702 exposure increased to 1.0 in day 4 at 5
No. 758 exposure increased to 4.0 in day 4 at 5
No. 956 exposure increased to 1.0 in day 4 at 5
No. 958 exposure increased to 2.0 in day 4 at 5
No. 959 exposure increased to 1.0 in day 4 at 5
No. 976 exposure increased to 2.0 in day 4 at 5
No. 978 exposure increased to 2.0 in day 4 at 5
  152/10000 [..............................] - ETA: 17:57:40 - reward: 675.9421*When No. 21 infected, Exposure is 4.0 in day 4 at move 0
*When No. 61 infected, Exposure is 2.0 in day 4 at move 0
*When No. 204 infected, Exposure is 3.0 in day 4 at move 0
*When No. 758 infected, Exposure is 4.0 in day 4 at move 0
*When No. 958 infected, Exposure is 2.0 in day 4 at move 0
*When No. 190 infected, Exposure is 2.0 in day 4 at move 1
*When No. 327 infected, Exposure is 2.0 in day 4 at move 2
*When No. 58 infected, Exposure is 3.0 in day 4 at move 3
*When No. 246 infected, Exposure is 2.0 in day 4 at move 3
*When No. 230 infected, Exposure is 2.0 in day 4 at move 4
No. 85 exposure increased to 2.0 in day 4 at 5
No. 113 exposure increased to 3.0 in day 4 at 5
No. 243 exposure increased to 2.0 in day 4 at 5
No. 278 exposure increased to 2.0 in day 4 at 5
*When No. 431 infected, Exposure is 2.0 in day 4 at move 5
No. 475 exposure increased to 3.0 in day 4 at 5
No. 482 exposure increased to 3.0 in day 4 at 5
*When No. 484 infected, Exposure is 2.0 in day 4 at move 5
No. 569 exposure increased to 2.0 in day 4 at 5
No. 635 exposure increased to 1.0 in day 4 at 5
No. 686 exposure increased to 2.0 in day 4 at 5
No. 702 exposure increased to 2.0 in day 4 at 5
No. 724 exposure increased to 1.0 in day 4 at 5
No. 941 exposure increased to 1.0 in day 4 at 5
No. 956 exposure increased to 2.0 in day 4 at 5
No. 959 exposure increased to 2.0 in day 4 at 5
No. 976 exposure increased to 3.0 in day 4 at 5
No. 978 exposure increased to 3.0 in day 4 at 5
  153/10000 [..............................] - ETA: 17:54:44 - reward: 674.3105*When No. 956 infected, Exposure is 2.0 in day 4 at move 0
*When No. 959 infected, Exposure is 2.0 in day 4 at move 0
*When No. 976 infected, Exposure is 3.0 in day 4 at move 1
*When No. 482 infected, Exposure is 3.0 in day 4 at move 2
*When No. 278 infected, Exposure is 2.0 in day 4 at move 3
*When No. 475 infected, Exposure is 3.0 in day 4 at move 4
No. 85 exposure increased to 3.0 in day 4 at 5
*When No. 113 infected, Exposure is 3.0 in day 4 at move 5
No. 128 exposure increased to 2.0 in day 4 at 5
No. 243 exposure increased to 3.0 in day 4 at 5
No. 418 exposure increased to 1.0 in day 4 at 5
No. 569 exposure increased to 3.0 in day 4 at 5
No. 635 exposure increased to 2.0 in day 4 at 5
No. 686 exposure increased to 3.0 in day 4 at 5
No. 702 exposure increased to 3.0 in day 4 at 5
No. 724 exposure increased to 2.0 in day 4 at 5
No. 941 exposure increased to 2.0 in day 4 at 5
*When No. 978 infected, Exposure is 3.0 in day 4 at move 5
  154/10000 [..............................] - ETA: 17:50:43 - reward: 672.5406*When No. 243 infected, Exposure is 3.0 in day 4 at move 0
*When No. 569 infected, Exposure is 3.0 in day 4 at move 0
*When No. 85 infected, Exposure is 3.0 in day 4 at move 1
No. 128 exposure increased to 3.0 in day 4 at 1
No. 240 exposure increased to 2.0 in day 4 at 1
No. 418 exposure increased to 2.0 in day 4 at 1
No. 635 exposure increased to 3.0 in day 4 at 1
No. 686 exposure increased to 4.0 in day 4 at 1
*When No. 702 infected, Exposure is 3.0 in day 4 at move 1
No. 724 exposure increased to 3.0 in day 4 at 1
No. 783 exposure increased to 2.0 in day 4 at 1
No. 941 exposure increased to 3.0 in day 4 at 1
  155/10000 [..............................] - ETA: 17:44:57 - reward: 671.0137*When No. 128 infected, Exposure is 3.0 in day 4 at move 1
*When No. 686 infected, Exposure is 4.0 in day 4 at move 1
*When No. 418 infected, Exposure is 2.0 in day 4 at move 2
*When No. 941 infected, Exposure is 3.0 in day 4 at move 2
No. 240 exposure increased to 3.0 in day 4 at 5
No. 405 exposure increased to 1.0 in day 4 at 5
No. 635 exposure increased to 4.0 in day 4 at 5
No. 724 exposure increased to 4.0 in day 4 at 5
No. 783 exposure increased to 3.0 in day 4 at 5
  156/10000 [..............................] - ETA: 17:41:41 - reward: 670.0984*When No. 783 infected, Exposure is 3.0 in day 4 at move 0
No. 240 exposure increased to 4.0 in day 4 at 1
No. 405 exposure increased to 2.0 in day 4 at 1
*When No. 635 infected, Exposure is 4.0 in day 4 at move 1
*When No. 724 infected, Exposure is 4.0 in day 4 at move 1
  157/10000 [..............................] - ETA: 17:36:05 - reward: 668.8320*When No. 240 infected, Exposure is 4.0 in day 4 at move 3
No. 405 exposure increased to 3.0 in day 4 at 5
  158/10000 [..............................] - ETA: 17:33:10 - reward: 668.1597*When No. 405 infected, Exposure is 3.0 in day 4 at move 2
  203/10000 [..............................] - ETA: 14:54:36 - reward: 701.4776No. 63 exposure increased to 1.0 in day 4 at 1
  204/10000 [..............................] - ETA: 14:54:17 - reward: 702.2252No. 63 exposure increased to 2.0 in day 4 at 5
No. 70 exposure increased to 1.0 in day 4 at 5
No. 296 exposure increased to 1.0 in day 4 at 5
No. 477 exposure increased to 1.0 in day 4 at 5
No. 617 exposure increased to 1.0 in day 4 at 5
No. 771 exposure increased to 1.0 in day 4 at 5
No. 831 exposure increased to 2.0 in day 4 at 5
No. 878 exposure increased to 1.0 in day 4 at 5
  205/10000 [..............................] - ETA: 15:07:52 - reward: 702.9697No. 63 exposure increased to 3.0 in day 4 at 5
No. 70 exposure increased to 2.0 in day 4 at 5
No. 94 exposure increased to 1.0 in day 4 at 5
No. 296 exposure increased to 2.0 in day 4 at 5
No. 477 exposure increased to 2.0 in day 4 at 5
No. 582 exposure increased to 1.0 in day 4 at 5
No. 615 exposure increased to 1.0 in day 4 at 5
No. 617 exposure increased to 2.0 in day 4 at 5
No. 771 exposure increased to 2.0 in day 4 at 5
No. 800 exposure increased to 1.0 in day 4 at 5
No. 831 exposure increased to 3.0 in day 4 at 5
No. 878 exposure increased to 2.0 in day 4 at 5
No. 887 exposure increased to 1.0 in day 4 at 5
  206/10000 [..............................] - ETA: 15:22:14 - reward: 703.5621*When No. 617 infected, Exposure is 2.0 in day 4 at move 1
*When No. 63 infected, Exposure is 3.0 in day 4 at move 2
*When No. 831 infected, Exposure is 3.0 in day 4 at move 3
*When No. 477 infected, Exposure is 2.0 in day 4 at move 4
No. 60 exposure increased to 2.0 in day 4 at 5
No. 70 exposure increased to 3.0 in day 4 at 5
No. 80 exposure increased to 1.0 in day 4 at 5
No. 94 exposure increased to 2.0 in day 4 at 5
No. 296 exposure increased to 3.0 in day 4 at 5
No. 311 exposure increased to 1.0 in day 4 at 5
No. 368 exposure increased to 1.0 in day 4 at 5
No. 582 exposure increased to 2.0 in day 4 at 5
No. 615 exposure increased to 2.0 in day 4 at 5
No. 771 exposure increased to 3.0 in day 4 at 5
No. 800 exposure increased to 2.0 in day 4 at 5
No. 863 exposure increased to 1.0 in day 4 at 5
No. 878 exposure increased to 3.0 in day 4 at 5
No. 887 exposure increased to 2.0 in day 4 at 5
  207/10000 [..............................] - ETA: 15:29:14 - reward: 704.0850*When No. 70 infected, Exposure is 3.0 in day 4 at move 0
*When No. 296 infected, Exposure is 3.0 in day 4 at move 1
*When No. 878 infected, Exposure is 3.0 in day 4 at move 1
*When No. 60 infected, Exposure is 2.0 in day 4 at move 4
*When No. 771 infected, Exposure is 3.0 in day 4 at move 4
No. 80 exposure increased to 2.0 in day 4 at 5
No. 82 exposure increased to 1.0 in day 4 at 5
No. 94 exposure increased to 3.0 in day 4 at 5
No. 145 exposure increased to 1.0 in day 4 at 5
No. 236 exposure increased to 1.0 in day 4 at 5
No. 311 exposure increased to 2.0 in day 4 at 5
No. 368 exposure increased to 2.0 in day 4 at 5
No. 474 exposure increased to 1.0 in day 4 at 5
No. 582 exposure increased to 3.0 in day 4 at 5
No. 615 exposure increased to 3.0 in day 4 at 5
No. 632 exposure increased to 1.0 in day 4 at 5
No. 669 exposure increased to 1.0 in day 4 at 5
No. 758 exposure increased to 1.0 in day 4 at 5
No. 800 exposure increased to 3.0 in day 4 at 5
No. 848 exposure increased to 1.0 in day 4 at 5
No. 853 exposure increased to 1.0 in day 4 at 5
No. 863 exposure increased to 2.0 in day 4 at 5
No. 877 exposure increased to 1.0 in day 4 at 5
No. 887 exposure increased to 3.0 in day 4 at 5
No. 953 exposure increased to 1.0 in day 4 at 5
  208/10000 [..............................] - ETA: 15:43:18 - reward: 705.0567*When No. 800 infected, Exposure is 3.0 in day 4 at move 0
*When No. 615 infected, Exposure is 3.0 in day 4 at move 3
*When No. 887 infected, Exposure is 3.0 in day 4 at move 3
No. 80 exposure increased to 3.0 in day 4 at 5
No. 82 exposure increased to 2.0 in day 4 at 5
*When No. 94 infected, Exposure is 3.0 in day 4 at move 5
No. 145 exposure increased to 2.0 in day 4 at 5
No. 193 exposure increased to 1.0 in day 4 at 5
No. 236 exposure increased to 2.0 in day 4 at 5
No. 291 exposure increased to 1.0 in day 4 at 5
*When No. 311 infected, Exposure is 2.0 in day 4 at move 5
No. 368 exposure increased to 3.0 in day 4 at 5
No. 382 exposure increased to 1.0 in day 4 at 5
No. 415 exposure increased to 1.0 in day 4 at 5
No. 433 exposure increased to 1.0 in day 4 at 5
No. 471 exposure increased to 1.0 in day 4 at 5
No. 474 exposure increased to 2.0 in day 4 at 5
No. 496 exposure increased to 2.0 in day 4 at 5
No. 576 exposure increased to 1.0 in day 4 at 5
No. 582 exposure increased to 4.0 in day 4 at 5
No. 632 exposure increased to 2.0 in day 4 at 5
No. 669 exposure increased to 2.0 in day 4 at 5
No. 758 exposure increased to 2.0 in day 4 at 5
No. 829 exposure increased to 1.0 in day 4 at 5
No. 848 exposure increased to 2.0 in day 4 at 5
No. 853 exposure increased to 2.0 in day 4 at 5
No. 863 exposure increased to 3.0 in day 4 at 5
No. 872 exposure increased to 1.0 in day 4 at 5
No. 877 exposure increased to 2.0 in day 4 at 5
No. 953 exposure increased to 2.0 in day 4 at 5
  209/10000 [..............................] - ETA: 16:01:23 - reward: 706.3254No. 80 exposure increased to 4.0 in day 4 at 1
No. 82 exposure increased to 3.0 in day 4 at 1
No. 90 exposure increased to 1.0 in day 4 at 1
No. 145 exposure increased to 3.0 in day 4 at 1
No. 193 exposure increased to 2.0 in day 4 at 1
No. 236 exposure increased to 3.0 in day 4 at 1
No. 291 exposure increased to 2.0 in day 4 at 1
No. 368 exposure increased to 4.0 in day 4 at 1
No. 382 exposure increased to 2.0 in day 4 at 1
No. 415 exposure increased to 2.0 in day 4 at 1
No. 433 exposure increased to 2.0 in day 4 at 1
No. 471 exposure increased to 2.0 in day 4 at 1
No. 474 exposure increased to 3.0 in day 4 at 1
No. 496 exposure increased to 3.0 in day 4 at 1
No. 576 exposure increased to 2.0 in day 4 at 1
No. 582 exposure increased to 5.0 in day 4 at 1
*When No. 632 infected, Exposure is 2.0 in day 4 at move 1
No. 669 exposure increased to 3.0 in day 4 at 1
No. 732 exposure increased to 1.0 in day 4 at 1
No. 733 exposure increased to 2.0 in day 4 at 1
No. 758 exposure increased to 3.0 in day 4 at 1
No. 829 exposure increased to 2.0 in day 4 at 1
No. 848 exposure increased to 3.0 in day 4 at 1
No. 853 exposure increased to 3.0 in day 4 at 1
No. 863 exposure increased to 4.0 in day 4 at 1
No. 872 exposure increased to 2.0 in day 4 at 1
No. 877 exposure increased to 3.0 in day 4 at 1
No. 905 exposure increased to 1.0 in day 4 at 1
*When No. 953 infected, Exposure is 2.0 in day 4 at move 1
  210/10000 [..............................] - ETA: 16:04:36 - reward: 707.1533*When No. 80 infected, Exposure is 4.0 in day 4 at move 0
*When No. 145 infected, Exposure is 3.0 in day 4 at move 0
*When No. 236 infected, Exposure is 3.0 in day 4 at move 0
*When No. 382 infected, Exposure is 2.0 in day 4 at move 0
*When No. 471 infected, Exposure is 2.0 in day 4 at move 0
*When No. 733 infected, Exposure is 2.0 in day 4 at move 0
No. 27 exposure increased to 1.0 in day 4 at 1
*When No. 82 infected, Exposure is 3.0 in day 4 at move 1
No. 90 exposure increased to 2.0 in day 4 at 1
No. 96 exposure increased to 1.0 in day 4 at 1
No. 193 exposure increased to 3.0 in day 4 at 1
No. 291 exposure increased to 3.0 in day 4 at 1
No. 344 exposure increased to 2.0 in day 4 at 1
No. 368 exposure increased to 5.0 in day 4 at 1
No. 387 exposure increased to 2.0 in day 4 at 1
No. 415 exposure increased to 3.0 in day 4 at 1
No. 433 exposure increased to 3.0 in day 4 at 1
No. 474 exposure increased to 4.0 in day 4 at 1
No. 496 exposure increased to 4.0 in day 4 at 1
No. 576 exposure increased to 3.0 in day 4 at 1
*When No. 582 infected, Exposure is 5.0 in day 4 at move 1
No. 669 exposure increased to 4.0 in day 4 at 1
No. 697 exposure increased to 1.0 in day 4 at 1
No. 732 exposure increased to 2.0 in day 4 at 1
No. 758 exposure increased to 4.0 in day 4 at 1
No. 829 exposure increased to 3.0 in day 4 at 1
No. 848 exposure increased to 4.0 in day 4 at 1
No. 853 exposure increased to 4.0 in day 4 at 1
No. 863 exposure increased to 5.0 in day 4 at 1
*When No. 872 infected, Exposure is 2.0 in day 4 at move 1
No. 877 exposure increased to 4.0 in day 4 at 1
No. 890 exposure increased to 2.0 in day 4 at 1
No. 905 exposure increased to 2.0 in day 4 at 1
  211/10000 [..............................] - ETA: 16:09:39 - reward: 707.7095*When No. 368 infected, Exposure is 5.0 in day 4 at move 0
*When No. 848 infected, Exposure is 4.0 in day 4 at move 0
No. 27 exposure increased to 2.0 in day 4 at 1
No. 90 exposure increased to 3.0 in day 4 at 1
No. 92 exposure increased to 1.0 in day 4 at 1
No. 96 exposure increased to 2.0 in day 4 at 1
No. 131 exposure increased to 1.0 in day 4 at 1
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># scores = dqn.test(env, nb_episodes = 1, visualize = False)</span>
<span class="c1"># print(np.mean(scores.history[&#39;episode_reward&#39;]))</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Test the agent</span>
<span class="kn">import</span> <span class="nn">tensorflow</span> <span class="k">as</span> <span class="nn">tf</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">reset</span><span class="p">()</span>
<span class="n">economy</span> <span class="o">=</span> <span class="mi">0</span>
<span class="n">states</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">day</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">10</span><span class="p">):</span>
    <span class="n">state</span> <span class="o">=</span> <span class="n">current_state</span><span class="p">(</span><span class="n">df</span><span class="p">)</span>
    <span class="n">states</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">state</span><span class="p">)</span>
    
    <span class="n">state</span> <span class="o">=</span> <span class="n">tf</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="n">state</span><span class="p">,</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">6</span><span class="p">])</span>
    
    <span class="n">prediction</span> <span class="o">=</span> <span class="n">model</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">state</span><span class="p">,</span> <span class="n">steps</span> <span class="o">=</span> <span class="mi">1</span><span class="p">)</span>
    <span class="n">action_by_agent</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">argmax</span><span class="p">(</span><span class="n">prediction</span><span class="p">)</span>
    <span class="n">df</span> <span class="o">=</span> <span class="n">one_day</span><span class="p">(</span><span class="n">df</span><span class="p">,</span> <span class="n">action</span> <span class="o">=</span> <span class="n">action_by_agent</span><span class="p">)</span>
    <span class="n">gain</span> <span class="o">=</span> <span class="n">economy_gain</span><span class="p">(</span><span class="n">df</span><span class="p">)</span>
    <span class="n">economy</span> <span class="o">+=</span> <span class="n">gain</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">f</span><span class="s2">&quot;Day </span><span class="si">{day}</span><span class="s2">: take action </span><span class="si">{action_by_agent}</span><span class="s2">, total_reward: </span><span class="si">{economy}</span><span class="s2">. </span><span class="si">{prediction}</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[96]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">model</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="s2">&quot;model_ann_4_6_states&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>INFO:tensorflow:Assets written to: model_ann_4_6_states/assets
</pre>
</div>
</div>

</div>
</div>

</div>
    </div>
  </div>
</body>

 


</html>

