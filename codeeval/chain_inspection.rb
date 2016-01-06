require "set"
File.open(ARGV[0]).each_line do |line|
    e = line.chomp.split(";").each_with_object(Hash.new) {|x, e|
        s, t = x.split("-")
        e[s] = t
    }
    puts e.size.times.each_with_object(Set.new).inject("BEGIN") {|c, v, _|
        if c.nil? || !e.has_key?(c) || v.member?(e[c])
            nil
        else
            v << e[c]
            e[c]
        end
    } == "END" ? "GOOD" : "BAD"
end
