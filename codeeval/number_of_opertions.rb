require 'set'
File.open(ARGV[0]).each_line do |line|
    nums = line.split.map(&:to_i)
    puts nums.permutation.any? {|perm|
           perm.drop(1).inject([perm[0]].to_set) {|r, x|
                r.each_with_object(Set.new) {|val, new|
                    new.merge([val + x, val - x, val * x])
                }
           }.member?(42)} ? "YES" : "NO"
end
