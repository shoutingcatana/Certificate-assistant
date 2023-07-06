{
  inputs.nixpkgs.url = "nixpkgs";
  outputs = {self, nixpkgs, }: let
    pkgs = nixpkgs.legacyPackages.x86_64-linux;
    python = pkgs.python310;
    customtkinter = python.pkgs.buildPythonPackage rec {
      src = pkgs.fetchPypi {
        inherit format pname version;
        python = "py3";
        dist = "py3";
        hash = "sha256-+LLbGJlZAzU5iE1/r/meu7ZUwYCX12HthEGA4y8LWSk=";
      };
      pname = "customtkinter";
      version = "5.2.0";
      format = "wheel";
      propagatedBuildInputs = [
        darkdetect
      ];
    };
    darkdetect = python.pkgs.buildPythonPackage rec {
      src = pkgs.fetchPypi {
        inherit format pname version;
        python = "py3";
        dist = "py3";
        hash = "sha256-p1Ccz1F+qtkrMcIU9ZPbzxOOqKQ7KTVAa71WXhVSeoU=";
      };
      pname = "darkdetect";
      version = "0.8.0";
      format = "wheel";
    };
    myPython = pkgs.python310.withPackages (ps: [
      ps.tkinter
      ps.openai
      customtkinter
    ]);
  in {
    devShells.x86_64-linux.default = pkgs.mkShell {
      packages = [
        myPython
      ];
    };
  };
}
