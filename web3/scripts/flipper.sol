// SPDX-Lience-Identifier: Apache-2.0
contract flipper {
      bool private value;

      /// Constructor: runs once when the contract is deployed.
      constructor(bool initvalue) {
          value = initvalue;
      }

      /// A "write" function: flips the stored value.
      function flip() public {
          value = !value;
      }

      /// A "read" function: returns the current value.
      function get() public view returns (bool) {
          return value;
      }
}
