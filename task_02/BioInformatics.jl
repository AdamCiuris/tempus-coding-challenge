### A Pluto.jl notebook ###
# v0.19.11

using Markdown
using InteractiveUtils

# ╔═╡ aa96bc58-2be4-11ed-3820-656ec59cf1a9

begin
import Shuffle
# map of complements for DNA pairs	
comps = Dict('a' => 't', 'A' => 'T', 'c' => 'g', 'C' => 'G', 't' => 'a', 'T' => 'A', 'g' => 'c', 'G' => 'C')
	
▷(x, y) = y(x) 

#=
calls standard library reverse for string reversal
=#
function reverse(strand::String) 
	return Base.reverse(strand) 
end

#=
Shuffled sequences can be used to evaluate the significance of sequence analysis results,
=#
function shuffle(strand::String) 
	return String(Shuffle.shuffle(strand))
end
	
#=
returns the complements of the given dna strand
note that a complement is upside down and needs to be reversed
=#
function complement(strand::String) 
	n = ""
	iter = Iterators.reverse(strand) # doing this because im unsure if a new iterator will be made per loop
		for s in iter # for "upside-down" dna strand
			n = n*comps[s] # concats each key value bind from comps dict
		end
	return n
end

#=
returns the pairs for a given half strand of DNA
followed by a line break \n
followed by the given string on the new line.
=#
function dsDNA(strand::String)
	upper = strand ▷ complement ▷ reverse
	lower = strand
	return (upper * "\n" * lower)
end
end #first begin

# ╔═╡ f636964a-b6d3-4df4-aac3-87890d677ece
begin
	dsDNA("atcgatGGGatctgac") ▷ Text 
end

# ╔═╡ 5b0b4791-7ece-4d01-89a5-249487e6a2d3
begin
	shuffle("atcgatGGGatctgac") ▷ Text 
end

# ╔═╡ 00000000-0000-0000-0000-000000000001
PLUTO_PROJECT_TOML_CONTENTS = """
[deps]
Shuffle = "bf21e494-c40e-4daa-abfb-de5ec0aad010"

[compat]
Shuffle = "~0.1.1"
"""

# ╔═╡ 00000000-0000-0000-0000-000000000002
PLUTO_MANIFEST_TOML_CONTENTS = """
# This file is machine-generated - editing it directly is not advised

[[Random]]
deps = ["Serialization"]
uuid = "9a3f8284-a2c9-5f02-9a11-845980a1fd5c"

[[Serialization]]
uuid = "9e88b42a-f829-5b0c-bbe9-9e923198166b"

[[Shuffle]]
deps = ["Random"]
git-tree-sha1 = "b812fb30d6d8b295b71dd5a4102d1ae7b60698e3"
uuid = "bf21e494-c40e-4daa-abfb-de5ec0aad010"
version = "0.1.1"
"""

# ╔═╡ Cell order:
# ╠═aa96bc58-2be4-11ed-3820-656ec59cf1a9
# ╠═f636964a-b6d3-4df4-aac3-87890d677ece
# ╠═5b0b4791-7ece-4d01-89a5-249487e6a2d3
# ╟─00000000-0000-0000-0000-000000000001
# ╟─00000000-0000-0000-0000-000000000002
