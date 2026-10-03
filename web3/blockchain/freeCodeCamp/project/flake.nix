{
  description = "Foundry project";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};

      # ── Compiler for this project ───────────────────────────────────────
      # Change this one string to pin the Solidity version. Either "nixpkgs"
      # (whatever this flake's nixpkgs carries — currently 0.8.33) or a key of
      # knownSolc below.
      #
      # Following a course written for 0.6.x? Set "0.6.12". Nothing else in the
      # project needs to change, and no other project is affected: foundry.toml
      # holds no compiler path, the shell supplies it via FOUNDRY_SOLC.
      solcVersion = "0.6.12";

      # version -> sha256 of that release's solc-static-linux asset.
      # Upstream's Linux binaries are statically linked, so they run on NixOS
      # unpatched. Add more with:
      #   nix-prefetch-url https://github.com/ethereum/solidity/releases/download/v<VER>/solc-static-linux
      knownSolc = {
        "0.6.12" = "f6cb519b01dabc61cab4c184a3db11aa591d18151e362fcae850e42cffdfb09a";
      };

      # Deliberately duplicated from the host config's pkgs/solc-bin.nix rather
      # than imported: it keeps this project buildable by anyone with plain Nix,
      # not just on the machine whose home-manager config defines that package.
      solcBin = version: sha256:
        let
          src = pkgs.fetchurl {
            url = "https://github.com/ethereum/solidity/releases/download/v${version}/solc-static-linux";
            inherit sha256;
          };
        in
        pkgs.runCommandLocal "solc-${version}" { } ''
          mkdir -p "$out/bin"
          cp ${src} "$out/bin/solc-${version}"
          chmod +x "$out/bin/solc-${version}"
        '';

      solc =
        if solcVersion == "nixpkgs" then {
          pkg = pkgs.solc;
          exe = "solc";
        } else {
          pkg = solcBin solcVersion knownSolc.${solcVersion};
          exe = "solc-${solcVersion}";
        };
    in
    {
      devShells.${system}.default = pkgs.mkShell {
        packages = [
          pkgs.foundry # forge, cast, anvil, chisel
          pkgs.just
          pkgs.jq # the justfile's deploy recipe parses forge's --json output
          solc.pkg
        ];

        # The whole per-project pinning mechanism, in one line. forge reads this
        # and skips its own ~/.svm downloader entirely.
        FOUNDRY_SOLC = "${solc.pkg}/bin/${solc.exe}";

        shellHook = ''
          echo "foundry $(forge --version | head -1 | cut -d' ' -f2) | solc $("$FOUNDRY_SOLC" --version | tail -1 | cut -d' ' -f2)"
        '';
      };
    };
}
