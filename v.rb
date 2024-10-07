# This is a Ruby on Rails model using ActiveRecord
class User < ApplicationRecord
  # Using the serialize method without specifying a serialization format, defaults to YAML
  #ruleid: test-rule-ruby
  serialize :preferences, Hash

  attr_accessible :signature_html, :user_id, :ticket_permission, :occasional

  # Other model methods and validations
end
