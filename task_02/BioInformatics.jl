### A Pluto.jl notebook ###
# v0.19.11

using Markdown
using InteractiveUtils

# ╔═╡ aa96bc58-2be4-11ed-3820-656ec59cf1a9
begin
▷(x, y) = y(x) 
function reverse(p) 
	return p
end

function compliment(p) 
	
	return p
end

#=
returns the pairs for a given half strand of DNA
followed by a line break \n
followed by the given string on the new line.
=#
function dsDNA(strand)
	upper = strand ▷ compliment ▷ reverse
	lower = strand
	return (upper * "\n" * lower)
end
end #module

# ╔═╡ f636964a-b6d3-4df4-aac3-87890d677ece

begin
	dsDNA("asdf") ▷ Text 
end

# ╔═╡ Cell order:
# ╠═aa96bc58-2be4-11ed-3820-656ec59cf1a9
# ╠═f636964a-b6d3-4df4-aac3-87890d677ece
