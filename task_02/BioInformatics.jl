### A Pluto.jl notebook ###
# v0.19.11

using Markdown
using InteractiveUtils

# ╔═╡ aa96bc58-2be4-11ed-3820-656ec59cf1a9
begin
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
returns the complements of the given dna strand
note that a complement is upside down and needs to be reversed
=#
function complement(strand::String) 
	n = ""
	
		for s in Iterators.reverse(strand) # for "upside-down" dna strand
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

# ╔═╡ Cell order:
# ╠═aa96bc58-2be4-11ed-3820-656ec59cf1a9
# ╠═f636964a-b6d3-4df4-aac3-87890d677ece
