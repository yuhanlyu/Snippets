require 'set'
File.open(ARGV[0]).each_line do |line|
    alpha = line.gsub(/[^[:alpha:]]/, "").downcase.chars.to_set
    ans = ('a'..'z').each.select {|c| !alpha.member?(c)}.join
    puts ans.size > 0 ? ans : "NULL"
end
