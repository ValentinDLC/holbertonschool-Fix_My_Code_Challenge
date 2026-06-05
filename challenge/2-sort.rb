puts ARGV.select { |a| a.match?(/^-?[0-9]+$/) }.map(&:to_i).sort
