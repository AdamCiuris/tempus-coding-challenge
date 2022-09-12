<h2>Julia Pluto Notebook Exposition</h2>

<h2>how to run</h2>

<h3>Docker</h3>

With docker installed and running, navigate to the dockerfile's directory and run: 

```docker build -t dockerfile .```

Then, with your local port 1234 unused, run the container with this command in the same directory: 

```docker run --detach --publish=1234:1234 dockerfile```

That's it! Wait a few moments and visit http://localhost:1234/ 

You may have to navigate to the notebook in the container's /app directory.

<h3>Ubuntu 22</h3>

run ```sudo apt-get install julia```if your ubuntu version is supported otherwise, ```snap install --classic julia```

Enter julia REPL with ```julia```
type a "]" which puts you into package mode. Type ```add Pluto```.

Things should be usable now.

```julia
julia> using Pluto
julia> Pluto.run()
```

Use the localhost link to connect to the Pluto server and select your notebook. Browser extensions caused me issues so I used a fresh Firefox install.

Pluto creates some kind of server available on LAN to edit files much like a jupyter notebook.