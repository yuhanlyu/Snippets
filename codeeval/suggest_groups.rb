require "set"
all_interests = Set.new
friends, interests = {}, {}
File.open(ARGV[0]).each_line do |line|
    name, friend, interest = line.chomp.split(":")
    interest = interest ? interest.split(",").to_set : Set.new()
    friends[name], interests[name] = friend.split(","), interest
    all_interests.merge(interest)  if interest
end

friends.keys.sort.each {|user|
    interest = Hash.new {|h, k| h[k] = 0}
    friends[user].each {|friend|
        interests[friend].each {|i| interest[i] += 1} 
    }
    ans = interest.each_pair.with_object([]) {|(i, c), ans| 
        ans << i if !interests[user].member?(i) && c >= friends[user].size * 0.5
    }.sort.join(",")
    puts "#{user}:#{ans}" if ans.size > 0
}
