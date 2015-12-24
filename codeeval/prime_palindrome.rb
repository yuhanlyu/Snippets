require 'prime'
puts Prime.each(999).to_a.reverse.find {|p| p.to_s == p.to_s.reverse}
